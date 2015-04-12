from django.db import models

from oscar.apps.catalogue.abstract_models import AbstractCategory, AbstractProduct

from oscar.core.loading import  get_model


class Category(AbstractCategory):

    partner = models.ForeignKey('partner.Partner', null=True, blank=True)        

    """def __init__ (self, *args, **kwargs):

        super(Category, self).__init__(*args, **kwargs)

        self.partner = Partner(name = self.name)"""

class Product(AbstractProduct):
	weight = models.DecimalField(blank=False,default=0.0,max_digits=5,decimal_places=2)
	width = models.DecimalField(blank=False,default=0.0,max_digits=5,decimal_places=2)
	height = models.DecimalField(blank=False,default=0.0,max_digits=5,decimal_places=2)
	length = models.DecimalField(blank=False,default=0.0,max_digits=5,decimal_places=2)

from oscar.apps.catalogue.models import *

