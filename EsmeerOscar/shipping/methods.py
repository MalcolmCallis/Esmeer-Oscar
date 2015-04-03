from oscar.apps.shipping import methods
from decimal import Decimal as D
from oscar.core import prices
import requests
import xml.etree.ElementTree as ET

class StandardPost(methods.Base):
    code = 'standardpost'
    name = 'USPS Standard Post Shipping'
    description = "Delivered within 2-8 business days"
    def calculate(self, basket):
        getShippingPrice(basket, "STANDARD POST")
        return prices.Price(
            currency=basket.currency,
            excl_tax=D('0.00'), incl_tax=D('20.00'))


class PriorityMail(methods.Base):
    code = 'prioritymail'
    name = 'USPS Priority Mail Shipping'
    description = "Delivered within 1-3 business days"
    def calculate(self, basket):
        getShippingPrice(basket, "PRIORITY")
        return prices.Price(
            currency=basket.currency,
            excl_tax=D('0.00'), incl_tax=D('20.00'))

class PriorityMailExpress(methods.Base):
    code = 'prioritymailexpress'
    name = 'USPS Priority Mail Express Shipping'
    description = "Delivered overnight"
    def calculate(self, basket):
        getShippingPrice(basket, "PRIORITY MAIL EXPRESS")
        return prices.Price(
            currency=basket.currency,
            excl_tax=D('0.00'), incl_tax=D('20.00'))

def getShippingPrice(basket, typeOfService, firstClassMailType = ""):
    start = 1
    uspsRequest = "http://production.shippingapis.com/ShippingAPI.dll?API=RateV4&XML=<RateV4Request USERID=\"167ESMEE3782\">"
    for item in basket.all_lines():
        uspsRequest += "<Package ID=\"" + str(start) + "\">"
        uspsRequest += "<Service>" + str(typeOfService) + "</Service>"
        uspsRequest += "<FirstClassMailType>" + str(firstClassMailType) + "</FirstClassMailType>"
        #Need to figure out how to get each product's vendor's zipcode...
        uspsRequest += "<ZipOrigination>43202</ZipOrigination>"
        #And also how to get the shipping zipcode
        uspsRequest += "<ZipDestination>90210</ZipDestination>"
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
    print r.text
    root = ET.fromstring(r.text)
    print root
    