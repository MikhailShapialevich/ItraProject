"""ItraProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from OurProject import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'OurProject' 

urlpatterns = [
    path('user/', include("OurProject.urls")),
    path('admin/', admin.site.urls),
    path('OurProject/', include('OurProject.urls')),
    path('personal/', views.personal),
    path('home/', views.home),
    path('shirt/', views.shirt),
    path('create_shirt/', views.create_shirt),
    #path(r'^$', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
