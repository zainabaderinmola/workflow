
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView

app_name = 'aifedayoscrumy'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aifedayoscrumy/', include('aifedayoscrumy.urls')),
    path('accounts/', include('allauth.urls')),
    path('index/', include(('aifedayoscrumy.urls', 'aifedayoscrumy'), 
                            namespace = 'aifedayoscrumy')),
    path('', TemplateView.as_view(template_name = 'home.html'), name = 'home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
