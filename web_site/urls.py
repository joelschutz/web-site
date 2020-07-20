"""umafoto_ae URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import portifolio.views
import umafoto_ae.views
import que_nome.views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portifolio.views.home, name='home'),
    path('umafoto-ae/', umafoto_ae.views.home, name='umafoto-ae'),
    path('umafoto-ae/result/', umafoto_ae.views.result, name='umafoto-ae-result'),
    path('umafoto-ae/info/', umafoto_ae.views.info, name='umafoto-ae-info'),
    path('que-nome/', que_nome.views.home, name='que-nome'),
    path('que-nome/team/', que_nome.views.team, name='que-nome-team'),
]

urlpatterns += staticfiles_urlpatterns()