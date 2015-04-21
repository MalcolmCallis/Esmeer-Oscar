from oscar.apps.shipping import methods
from decimal import Decimal as D
from oscar.core import prices

class VendorShipping(methods.Base):
    code = 'vendorshipping'
    name = 'Vendor Shipping'

    def calculate(self, basket):
        shippingPrice = 0.0
        for item in basket.all_lines():
            shippingPrice += float(item.product.shipping_price * basket.product_quantity(item.product))
        return prices.Price(
            currency=basket.currency,
            excl_tax=D('0.00'), incl_tax=D(shippingPrice))