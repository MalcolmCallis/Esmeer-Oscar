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


class ProductCreateUpdateView(CoreProductCreateUpdateView):
    def __init__(self, *args, **kwargs):
        super(ProductCreateUpdateView, self).__init__(*args, **kwargs)
        self.formsets = {'category_formset': self.category_formset,
                         'image_formset': self.image_formset,
                         'stockrecord_formset': self.stockrecord_formset}
