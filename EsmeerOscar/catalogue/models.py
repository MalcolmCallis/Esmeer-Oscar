from django.db import models

from oscar.apps.catalogue.abstract_models import AbstractCategory, AbstractProduct

from oscar.core.loading import  get_model


class Category(AbstractCategory):

    partner = models.ForeignKey('partner.Partner', null=True, blank=True)        

    """def __init__ (self, *args, **kwargs):

        super(Category, self).__init__(*args, **kwargs)

        self.partner = Partner(name = self.name)"""

class Product(AbstractProduct):
	shipping_price = models.DecimalField(max_digits=6, decimal_places=2, null=False)

from oscar.apps.catalogue.models import *

