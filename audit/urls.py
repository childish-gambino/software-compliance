"""audit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView # <--
from iaudit.views import user_landed
from allauth.account import views as allauth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    # path('', TemplateView.as_view(template_name="index.html"), name='home'),
    path('readme/', TemplateView.as_view(template_name="iaudit/readme.html"), name='readme'),
    path('admin/', admin.site.urls),
    # path('accounts/logout', include('allauth.urls'),name='logout'),
    path('accounts/', include('allauth.urls')),
    path('', user_landed, name='home'),
    path('api/', include('iaudit.urls')),
    # path('audi/', footprint,name='dash'), # for the dashboard
]
urlpatterns += staticfiles_urlpatterns()