from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.OrderListView.as_view(), name='order_list'),
    path('create/', views.CreateOrderView.as_view(), name='create_order'),
    path('update/<str:order_id>/', views.UpdateOrderView.as_view(), name='update_order'),
    path('delete/<str:order_id>/', views.DeleteOrderView.as_view(), name='delete_order'),
    path('get/<str:order_id>/', views.GetOrderView.as_view(), name='get_order'),
    path('api/orders/', views.OrdersAPIView.as_view(), name='orders_api'),
] 