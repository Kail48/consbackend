from django.urls import path
from . import views

urlpatterns = [
    path('document/',views.getuploadDocument),
    path('documents/',views.getDocuments),
    path('profiles/',views.getStudentProfiles),
    path('admin-documents/',views.getStudentDocuments),
    path('admin-verification/',views.verifyDocument),
    path('total-users/',views.getTotalUsers),
]
