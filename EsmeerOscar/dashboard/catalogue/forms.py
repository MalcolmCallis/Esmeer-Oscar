
from django import forms
from django.core import exceptions
from django.forms.models import inlineformset_factory
from django.utils.translation import ugettext_lazy as _
from treebeard.forms import MoveNodeForm, movenodeform_factory

from oscar.core.utils import slugify
from oscar.core.loading import get_class, get_model
from oscar.forms.widgets import ImageInput

from oscar.apps.dashboard.catalogue.forms import  BaseCategoryForm
from oscar.apps.dashboard.catalogue.forms import ProductForm as CoreProductForm

Category = get_model('catalogue', 'Category')
Product = get_model('catalogue', 'Product')
StockRecord = get_model('partner', 'StockRecord')
Partner = get_model('partner', 'Partner')

class StockRecordForm(forms.ModelForm):
         
    def __init__(self, product_class, user, *args, **kwargs):
        # The user kwarg is not used by stock StockRecordForm. We pass it
        # anyway in case one wishes to customise the partner queryset
        self.user = user
        super(StockRecordForm, self).__init__(*args, **kwargs)

        del self.fields['price_retail']
        del self.fields['cost_price']
        del self.fields['price_currency']
        

        # If not tracking stock, we hide the fields
        if not product_class.track_stock:
            del self.fields['num_in_stock']
            del self.fields['low_stock_threshold']
        else:
            self.fields['price_excl_tax'].required = True
            self.fields['num_in_stock'].required = True

        if not self.user.is_superuser: 
            
            partnerQuery = []

            for part in Partner.objects.all():
                for user in part.users.get_queryset():
                    if user == self.user:
                        partnerQuery.append(part.name)

            self.fields['partner'].queryset = Partner.objects.filter(name__in=partnerQuery) 

    class Meta:
        model = StockRecord
        exclude = ('product', 'num_allocated')

BaseStockRecordFormSet = inlineformset_factory(
            Product, StockRecord, form=StockRecordForm, extra=1)


class StockRecordFormSet(BaseStockRecordFormSet):

    def __init__(self, product_class, user, *args, **kwargs):
        self.user = user
        self.require_user_stockrecord = not user.is_staff
        self.product_class = product_class
        super(StockRecordFormSet, self).__init__(*args, **kwargs)
        self.set_initial_data()

    def set_initial_data(self):
        """
        If user has only one partner associated, set the first
        stock record's partner to it. Can't pre-select for staff users as
        they're allowed to save a product without a stock record.

        This is intentionally done after calling __init__ as passing initial
        data to __init__ creates a form for each list item. So depending on
        whether we can pre-select the partner or not, we'd end up with 1 or 2
        forms for an unbound form.
        """
        if self.require_user_stockrecord:
            try:
                user_partner = self.user.partners.get()
            except (exceptions.ObjectDoesNotExist,
                    exceptions.MultipleObjectsReturned):
                pass
            else:
                partner_field = self.forms[0].fields.get('partner', None)
                if partner_field and partner_field.initial is None:
                    partner_field.initial = user_partner

    def _construct_form(self, i, **kwargs):
        kwargs['product_class'] = self.product_class
        kwargs['user'] = self.user
        return super(StockRecordFormSet, self)._construct_form(
            i, **kwargs)


    def clean(self):
        """
        If the user isn't a staff user, this validation ensures that at least
        one stock record's partner is associated with a users partners.
        """
        if any(self.errors):
            return
        if self.require_user_stockrecord:
            stockrecord_partners = set([form.cleaned_data.get('partner', None)
                                        for form in self.forms])
        user_partners = set(self.user.partners.all())
        if not user_partners & stockrecord_partners:
            raise exceptions.ValidationError(
                _("At least one stock record must be set to a partner that"
                "you're associated with."))


CategoryForm = movenodeform_factory(Category, form=BaseCategoryForm, exclude=('partner',) )

class ProductForm(CoreProductForm):
    class Meta:
        model = Product
        fields = ['title', 'upc', 'description', 'shipping_price']
        widgets = {
            'structure': forms.HiddenInput()
        }
