from django.urls import path

from . import views


urlpatterns = [
    path('sentimentanalysis', views.home, name='home-url'),
    path('search', views.createpost, name='sentiment-url'),

]