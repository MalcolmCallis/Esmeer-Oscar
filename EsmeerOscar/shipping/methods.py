from oscar.apps.shipping import methods
from decimal import Decimal as D
from oscar.core import prices
import requests
import xml.etree.ElementTree as ET
from oscar.core.loading import get_model, get_class

Partner = get_model('partner', 'Partner')
StockRecord = get_model('partner', 'StockRecord')
PartnerAddress = get_model('partner', 'PartnerAddress')

class PriorityMail(methods.Base):

    def __init__(self, zipcode):
        super(methods.Base, self).__init__()
        self.zipcode = zipcode

    code = 'prioritymail'
    name = 'USPS Priority Mail Shipping'
    description = "Delivered within 1-3 business days"
    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=D('0.00'), incl_tax=D(getShippingPrice(basket, "PRIORITY", self.zipcode)))

class PriorityMailExpress(methods.Base):

    def __init__(self, zipcode):
        super(methods.Base, self).__init__()
        self.zipcode = zipcode

    code = 'prioritymailexpress'
    name = 'USPS Priority Mail Express Shipping'
    description = "Delivered overnight"
    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=D('0.00'), incl_tax=D(getShippingPrice(basket, "PRIORITY MAIL EXPRESS", self.zipcode)))

def getShippingPrice(basket, typeOfService, zipcode):
    start = 1
    uspsRequest = "http://production.shippingapis.com/ShippingAPI.dll?API=RateV4&XML=<RateV4Request USERID=\"167ESMEE3782\">"
    for item in basket.all_lines():

        uspsRequest += "<Package ID=\"" + str(start) + "\">"
        uspsRequest += "<Service>" + str(typeOfService) + "</Service>"
        uspsRequest += "<FirstClassMailType></FirstClassMailType>"

        tempStockRecord = StockRecord.objects.get(product=item.product)
        tempAddress = PartnerAddress.objects.get(partner=tempStockRecord.partner)
        uspsRequest += "<ZipOrigination>" + tempAddress.postcode + "</ZipOrigination>"
        print "Origin Zip"
        print tempAddress.postcode
        
        print "Dest Zip"
        print zipcode
        #And also how to get the shipping zipcode
        uspsRequest += "<ZipDestination>" + zipcode + "</ZipDestination>"
        totalWeight = basket.product_quantity(item.product) * item.product.weight
        pounds,oz = divmod(totalWeight, 1)
        oz = oz * 16
        uspsRequest += "<Pounds>" + str(pounds) + "</Pounds>"
        uspsRequest += "<Ounces>" + str(oz) + "</Ounces>"
        #How to determine shape of box?
        if item.product.length >= 12 or item.product.width >= 12 or item.product.height >= 12:
            uspsRequest += "<Container>RECTANGULAR</Container>"
            uspsRequest += "<Size>LARGE</Size>"
        else:
            uspsRequest += "<Container></Container>"
            uspsRequest += "<Size>REGULAR</Size>"

        uspsRequest += "<Width>" + str(item.product.width) + "</Width>"
        uspsRequest += "<Length>" + str(item.product.length) + "</Length>"
        uspsRequest += "<Height>" + str(item.product.height) + "</Height>"
        uspsRequest += "<Machinable>TRUE</Machinable>"
        uspsRequest += "</Package>"

        start += 1

    uspsRequest += "</RateV4Request>"
    r = requests.post(uspsRequest)
    r.encoding = 'UTF-8'
    root = ET.fromstring(r.text)
    price = 0.0
    for rate in root.findall("./Package/Postage/Rate"):
        price += float(rate.text)
    return price