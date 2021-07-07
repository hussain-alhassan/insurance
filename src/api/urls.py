from django.urls import path
from . import views

urlpatterns = [
    path('v1/', views.api_overview, name='api-overview'),
    path('v1/customers', views.customer_list, name='customer-list'),
    path('v1/customers/<str:pk>', views.customer_detail, name='customer-detail'),
    path('v1/create_customer', views.customer_create, name='customer-create'),
    path('v1/update_customer/<str:pk>', views.customer_update, name='customer-update'),
    path('v1/delete_customer/<str:pk>', views.customer_delete, name='customer-delete'),
]
