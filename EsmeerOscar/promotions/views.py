from django.views.generic import TemplateView, RedirectView
from django.core.urlresolvers import reverse
from oscar.apps.promotions.views import HomeView as CoreHomeView
from oscar.core.loading import get_classes, get_model

Partner = get_model('partner', 'Partner')
MAX_PARTNERS = 15

class HomeView(CoreHomeView):
    template_name = 'promotions/homepage.html'
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        num_partners = min(MAX_PARTNERS, Partner.objects.count())
        context['partners'] = Partner.objects.all()[:num_partners]
        return context
    

class ContactUsView(TemplateView):
    template_name = 'promotions/contactus.html'
    
