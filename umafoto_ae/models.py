from django.db import models
from wagtail.core.models import Page
from umafoto_ae.photohunter import PhotoHunter

# Create your models here.
class UmaFotoHome(Page):
    template = 'umafoto_ae/umafoto_ae_home.html'

class UmaFotoResult(Page):
    template = 'umafoto_ae/umafoto_ae_result.html'
    def get_context(self, request, *args, **kwargs):
        """ Page for teams """
        context = super().get_context(request, *args, **kwargs)
        context['ph'] = PhotoHunter(request).get_photo()
        return context

class UmaFotoInfo(Page):
    template = 'umafoto_ae/umafoto_ae_info.html'
