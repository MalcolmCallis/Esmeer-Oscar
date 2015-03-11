from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _, pgettext_lazy

from oscar.core.utils import get_default_currency
from oscar.core.compat import AUTH_USER_MODEL
from oscar.models.fields import AutoSlugField
from oscar.apps.partner.exceptions import InvalidStockAdjustment

from oscar.apps.partner.abstractmodels import AbstractStockRecord as CoreAbstractStockRecord

class AbstractStockRecord(CoreAbstractStockRecord):
    # Save method sets cost price and retail price equal to price excluding tax, so they are all the same
    # Create by Neil Madsen, March 10, 2015
    def save(self, *args, **kwargs):
        self.cost_price = self.price_excl_tax
        self.price_retail = self.price_excl_tax
        super(AbstractStockRecord, self).save(*args, **kwargs) # Call the "real" save() method.
        
