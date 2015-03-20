from django.conf.urls import patterns, include, url
from oscar.app import application
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from oscar.app import shop

from paypal.express.dashboard.app import application


urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.
    url(r'^admin/', include(admin.site.urls)),
    url(r'^checkout/paypal/', include('paypal.express.urls')),
    url(r'^dashboard/paypal/express/', include(application.urls)),
    url(r'', include(shop.urls)),
    url(r'', include(application.urls)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)