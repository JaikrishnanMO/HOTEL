from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('admin-login',views.admin_login,name='admin_login'),
    path('admin-home',views.Admin_home,name='Admin_home'),
    path('add-food',views.Add_food,name="Add_food"),
    path('view-food',views.view_food,name="view_food"),
    path('food/<int:item_id>/update/',views.update_food,name='update_food'),
    path('food/<int:item_id>/delete/',views.delete_food,name="delete_food"),
    path('today-menu',views.today_menu,name="today_menu"),
    path('view-todaymenu',views.view_today_menu,name="view_today_menu"),
    path('todayfood/<int:item_id>/delete/',views.delete_today_menu,name="delete_today_menu"),
    path('orders',views.view_orders,name="view_orders"),
    path('order/<int:order_id>/view/',views.view_order_item,name="view_order_item"),
    path('order/<int:food_id>/accept-payment/', views.accept_payment, name='accept_payment'),
    path('admin_logout',views.admin_logout,name="admin_logout"),
]
