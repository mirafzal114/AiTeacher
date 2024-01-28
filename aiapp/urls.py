from django.urls import path
from .views import ielts_checking_view, dict_view

urlpatterns = [
    path('', ielts_checking_view, name='home-page'),
    path('result/', ielts_checking_view, name='result'),
    path('dict/', dict_view, name='dictionary' )
]