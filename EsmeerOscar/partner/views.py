from django.views.generic import TemplateView, RedirectView
from django.core.urlresolvers import reverse
from oscar.core.loading import get_classes, get_model

Partner = get_model('partner', 'Partner')

class VendorView(TemplateView):
    template_name = 'partner/viewvendors.html'
    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['vendor'] = Partner.objects.all()[0]
