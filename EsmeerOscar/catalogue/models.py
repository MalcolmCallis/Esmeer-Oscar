from django.db import models

from oscar.apps.catalogue.abstract_models import AbstractProduct

class Product(AbstractProduct):
    weight = models.DecimalField(blank=False,default=0.0,max_digits=5,decimal_places=2)
    width = models.DecimalField(blank=False,default=0.0,max_digits=5,decimal_places=2)
    height = models.DecimalField(blank=False,default=0.0,max_digits=5,decimal_places=2)
    length = models.DecimalField(blank=False,default=0.0,max_digits=5,decimal_places=2)
from oscar.apps.catalogue.models import *