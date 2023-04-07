
from django.urls import path
from . import views

urlpatterns = [
    path('',views.test),
    path('add/',views.addTest),
      path('getc/<str:name>',views.getTest),
]
