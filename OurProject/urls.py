from django.contrib.auth import views
from django.urls import path, reverse_lazy
from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'OurProject'
urlpatterns = [
   url(r'^$', views.shirt_list, name='shirt_list'),
    url(r'^shirt/(?P<pk>\d+)/$', views.shirt_detail, name='shirt_detail'),
   #path('', views.shirt_list, name='shirt_list'),
   #path('shirt/<int:pk>/', views.shirt_detail, name='shirt_detail'),
   url('^', include('django.contrib.auth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)