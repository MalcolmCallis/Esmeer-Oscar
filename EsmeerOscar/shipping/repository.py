from oscar.apps.shipping import repository
from EsmeerOscar.shipping import methods
from oscar.core.loading import get_model, get_class

CheckoutSessionData = get_class(
    'checkout.utils', 'CheckoutSessionData')

class Repository(repository.Repository):
	
	def get_available_shipping_methods(self,basket,user=None,shipping_addr=None,request=None,**kwargs):
		checkout_session = CheckoutSessionData(request)
		addr_data = checkout_session.new_shipping_address_fields()
		shippingMethods = (methods.PriorityMail(zipcode=addr_data['postcode']),methods.PriorityMailExpress(zipcode=addr_data['postcode']))
		return shippingMethods