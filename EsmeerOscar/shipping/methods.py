from oscar.apps.shipping import methods
from decimal import Decimal as D
from oscar.core import prices

class Standard(methods.Base):
    code = 'standard'
    name = 'Standard shipping'
    description = "Delivered within 5-7 working days"
    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=D('0.00'), incl_tax=D('0.00'))
class Express(methods.Base):
    code = 'express'
    name = 'Express shipping'
    description = "Delivered within 2-3 working days"
    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=D('0.00'), incl_tax=D('20.00'))
