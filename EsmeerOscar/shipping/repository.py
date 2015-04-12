from oscar.apps.shipping import repository
from EsmeerOscar.shipping import methods
from oscar.core.loading import get_model, get_class

CheckoutSessionData = get_class(
    'checkout.utils', 'CheckoutSessionData')
UserAddress = get_model('address', 'UserAddress')

class Repository(repository.Repository):
	
	def get_available_shipping_methods(self,basket,user=None,shipping_addr=None,request=None,**kwargs):
		checkout_session = CheckoutSessionData(request)
		new_addr_data = checkout_session.new_shipping_address_fields()
		old_addr_data = checkout_session.shipping_user_address_id()
		if shipping_addr:
			print "Got shipping_addr"
			print shipping_addr
			shippingMethods = (methods.PriorityMail(zipcode=shipping_addr.postcode),methods.PriorityMailExpress(zipcode=shipping_addr.postcode))
		elif old_addr_data:

			#Exception will be thrown if User has items in the basket and changes
			#their address mid-session

			try:
				oldAddr = UserAddress._default_manager.get(pk=old_addr_data)
			except UserAddress.DoesNotExist:
				print "Exception Thrown, using default"
				shippingMethods = (methods.PriorityMail('43202'), methods.PriorityMailExpress('43202'))
				return shippingMethods

			shippingMethods = (methods.PriorityMail(zipcode=oldAddr.postcode),methods.PriorityMailExpress(zipcode=oldAddr.postcode))
		
		elif new_addr_data:
			print "Got new address"
			shippingMethods = (methods.PriorityMail(zipcode=new_addr_data['postcode']),methods.PriorityMailExpress(zipcode=new_addr_data['postcode']))
		else:
			print "Using Default"
			shippingMethods = (methods.PriorityMail('43202'), methods.PriorityMailExpress('43202'))

		return shippingMethods