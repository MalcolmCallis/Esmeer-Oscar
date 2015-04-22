from django.conf.urls import url, include

from oscar.core.application import Application
from oscar.core.loading import get_class
from oscar.apps.promotions.models import PagePromotion, KeywordPromotion

class PartnerApplication(Application):
    name = 'partner'

    vendor_view = get_class('partner.views', 'VendorView')

    def get_urls(self):
        urls = super(PartnerApplication, self).get_urls()
        urls += [
            url(r'^(?P<partner_code>[0-9A-Za-z_\-]+)$', self.vendor_view.as_view(), name='partnerView'),
        ]
        return self.post_process_urls(urls)


application = PartnerApplication()
