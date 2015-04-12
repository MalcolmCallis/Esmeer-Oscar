
from django import forms
from django.core import exceptions
from django.forms.models import inlineformset_factory
from django.utils.translation import ugettext_lazy as _
from treebeard.forms import MoveNodeForm, movenodeform_factory

from oscar.core.utils import slugify
from oscar.core.loading import get_class, get_model
from oscar.forms.widgets import ImageInput

from oscar.apps.dashboard.catalogue.forms import StockRecordForm as CoreStockRecordForm, BaseCategoryForm
from oscar.apps.dashboard.catalogue.forms import ProductForm as CoreProductForm

Category = get_model('catalogue', 'Category')
Product = get_model('catalogue', 'Product')

class StockRecordForm(CoreStockRecordForm):
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

CategoryForm = movenodeform_factory(Category, form=BaseCategoryForm, exclude=('partner',) )

class ProductForm(CoreProductForm):
    class Meta:
        model = Product
        fields = ['title', 'upc', 'description', 'weight', 'width', 'length', 'height']
        widgets = {
            'structure': forms.HiddenInput()
        }
