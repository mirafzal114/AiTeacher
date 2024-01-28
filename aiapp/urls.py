from django.contrib.auth.views import LoginView
from django.urls import path
from .views import ielts_checking_view,\
    dict_view,about,contact,service,advice_view,register_view,feedback_view

urlpatterns = [
    path('', ielts_checking_view, name='home-page'),
    path('result/', ielts_checking_view, name='result'),
    path('dict/', dict_view, name='dictionary'),
    path('about/', about, name='about-page'),
    path('contact/', contact, name='contact-page'),
    path('service/', service, name='service-page'),
    path('topic/', advice_view, name='advice'),
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(template_name='aiapp/login.html'), name='login'),
    path('feedback/', feedback_view, name='feedback')

]