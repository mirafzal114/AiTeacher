from django.urls import path
from .views import ielts_checking_view, dict_view,about,contact,service,advice_view

urlpatterns = [
    path('', ielts_checking_view, name='home-page'),
    path('result/', ielts_checking_view, name='result'),
    path('dict/', dict_view, name='dictionary'),
    path('about/', about, name='about-page'),
    path('contact/', contact, name='contact-page'),
    path('service/', service, name='service-page'),
    path('topic/', advice_view, name='advice')
]