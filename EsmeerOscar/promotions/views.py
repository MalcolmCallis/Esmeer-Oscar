from django.views.generic import TemplateView, RedirectView
from django.core.urlresolvers import reverse
from oscar.apps.promotions.views import HomeView as CoreHomeView

class HomeView(CoreHomeView):
    template_name = 'promotions/homepage.html'
