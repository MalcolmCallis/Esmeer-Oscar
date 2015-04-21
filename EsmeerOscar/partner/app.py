from django.conf.urls import url

from oscar.core.application import Application
from oscar.core.loading import get_class
from oscar.apps.promotions.models import PagePromotion, KeywordPromotion

class PartnerApplication(Application):
    name = 'partner'

    vendor_view = get_class('partner.views', 'VendorView')

    def get_urls(self):
        urls = [
            url(r'^(?P<partner_code>[\w-]*)$', self.vendor_view.as_view(), name='partnerView'),
        ]
        return self.post_process_urls(urls)


application = PartnerApplication()
