from django.urls import path
from . import views


urlpatterns = [
    path('user/',views.order_item,name="order_item"),
    path('user/menu',views.menu,name="menu"),
]
