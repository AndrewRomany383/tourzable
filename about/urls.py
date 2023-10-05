from django.urls import path
from . import api_view


app_name = 'about'

urlpatterns = [
    path('about', api_view.AboutData.as_view(), name='about'),
    path('about/ar', api_view.AboutDataAr.as_view(), name='about_ar'),
    path('faq', api_view.FaqData.as_view(), name='faq'),
    path('faq/ar', api_view.FaqDataAR.as_view(), name='faq_ar'),
    path('contact_us', api_view.Contactus.as_view(), name='contact_us'),
    path('contact_consultant', api_view.Contactconsultant.as_view(), name='contact_consultant'),
]