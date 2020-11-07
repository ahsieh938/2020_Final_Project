from django.urls import path
from .views import (
    InvoiceListView, InvoiceCreateView, 
    InvoiceUpdateView, InvoiceDeleteView, 
    OrderUpdateView, OrderDeleteView)
from . import views

urlpatterns = [
    path('list/', InvoiceListView.as_view(), name='inv-home'),
    path('new/', InvoiceCreateView.as_view(), name='inv-create'),
    path('search/', views.search, name='inv-search'),
    path('<str:pk>/update/', InvoiceUpdateView.as_view(), name='inv-update'),
    path('<str:pk>/delete/', InvoiceDeleteView.as_view(), name='inv-delete'),
    path("<str:invoice_num>/", views.detail, name="inv-detail"), 
    path('<str:invoice_num>/new_order_item/', views.order_create_view, name='inv-order-item'),
    path('order_update/<int:pk>', OrderUpdateView.as_view(), name='inv-order-update'),
    path('order_delete/<int:pk>', OrderDeleteView.as_view(), name='inv-order-delete'),
] 