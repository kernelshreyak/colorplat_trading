from django.urls import path

from . import views

# Super admin URLs
urlpatterns = [
    path('', views.index, name='index'),
    path('showpriceshome', views.showpriceshome, name='index')
]