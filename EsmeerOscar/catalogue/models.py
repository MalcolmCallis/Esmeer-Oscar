from django.db import models

from oscar.apps.catalogue.abstract_models import AbstractCategory

from oscar.core.loading import  get_model


class Category(AbstractCategory):

    partner = models.ForeignKey('partner.Partner', null=True, blank=True)        

    """def __init__ (self, *args, **kwargs):

        super(Category, self).__init__(*args, **kwargs)

        self.partner = Partner(name = self.name)"""

from oscar.apps.catalogue.models import *

