
from django.urls import path
from . import views

urlpatterns = [
    path('',views.test),
    path('add/',views.addTest),
    path('getc/<str:name>',views.getTest),
    path('add-university/',views.addUniversity),
    path('add-story/',views.addStory),
    path('university/',views.getUniversities),
    path('stories/',views.getStories)
]
