from django.views import generic
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import render_to_string

from oscar.core.loading import get_classes, get_model

from django_tables2 import SingleTableMixin

from oscar.views.generic import ObjectLookupView

from oscar.apps.dashboard.catalogue.views import ProductCreateUpdateView as CoreProductCreateUpdateView

Partner = get_model('partner', 'Partner')

Category = get_model('catalogue', 'Category')

ProductTable, CategoryTable \
    = get_classes('dashboard.catalogue.tables',
        ('ProductTable', 'CategoryTable'))

class ProductCreateUpdateView(CoreProductCreateUpdateView):
    def __init__(self, *args, **kwargs):
        super(ProductCreateUpdateView, self).__init__(*args, **kwargs)
        self.formsets = {'category_formset': self.category_formset,
                         'image_formset': self.image_formset,
                         'stockrecord_formset': self.stockrecord_formset}

class CategoryListView(SingleTableMixin, generic.TemplateView):

    template_name = 'dashboard/catalogue/category_list.html'
    table_class = CategoryTable
    context_table_name = 'categories'

    def get_queryset(self):

        currentUser = self.request.user

        partnersLinkedToCurrentUser = []

        for partner in Partner.objects.all():
            for user in partner.users.get_queryset():
                if user == currentUser:
                    partnersLinkedToCurrentUser.append(partner.name)

        if len(partnersLinkedToCurrentUser) is not 0:
            return Category.get_root_nodes().filter(name__in=partnersLinkedToCurrentUser)

        return Category.get_root_nodes()

    def get_context_data(self, *args, **kwargs):
        ctx = super(CategoryListView, self).get_context_data(*args, **kwargs)
        ctx['child_categories'] = Category.get_root_nodes()
        ctx['queryset_description'] = _("Categories")
        return ctx





