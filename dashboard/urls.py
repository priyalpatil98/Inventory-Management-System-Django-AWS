from django.urls import path
from . import views

urlpatterns = [
    #Index Page Url
    path('', views.index, name='dashboard-index'),

    #Staff Page Url
    path('staff/', views.staff, name='dashboard-staff'),

    path('product/', views.product, name='dashboard-product'),

    path('order/', views.order, name='dashboard-order'),



]