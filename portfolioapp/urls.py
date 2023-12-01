from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from . import views



urlpatterns=[
    path('',views.home,name='accueil'),
    path('service-detail/',views.service_detail,name='service-detail'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)