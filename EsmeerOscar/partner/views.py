from django.views.generic import TemplateView, RedirectView
from django.core.urlresolvers import reverse
from oscar.core.loading import get_classes, get_model

Partner = get_model('partner', 'Partner')
Product = get_model('catalogue', 'product')
StockRecord = get_model('partner', 'stockrecord')

class VendorView(TemplateView):
    template_name = 'partner/viewpartner.html'

    def get(self, request, partner_code,*args, **kwargs):
        self.object = partner_code
        return super(VendorView, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        partner = Partner.objects.get(code=self.object)
        context['partner'] = partner
        products = []
        for stockrecord in StockRecord.objects.filter(partner=partner):
            products.append(stockrecord.product)
        context['products'] = products
        return context
