from django.urls import path
from . import views

urlpatterns=[
    path('kitchen/',views.kitchen_log,name="kitchen_log"),
    path('kitchen/logout',views.kitchen_logout,name="kitchen_logout"),
    path('kitchen/home',views.kitchen_home, name="kitchen_home"),
    path('kitchen/<int:req_id>/view/',views.view_request,name="view_request"),
]