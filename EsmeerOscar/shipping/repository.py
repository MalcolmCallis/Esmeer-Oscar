from oscar.apps.shipping import repository
from EsmeerOscar.shipping import methods

class Repository(repository.Repository):
	
	def get_available_shipping_methods(self,basket,user=None,shipping_addr=None,request=None,**kwargs):
		shippingMethods = (methods.VendorShipping(),)
		return shippingMethods