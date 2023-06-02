from django.urls import path
from . import views

urlpatterns = [
    path('document/',views.getuploadDocument),
    path('documents/',views.getDocuments),
    path('student-documents/',views.getMyDocuments),
    path('profiles/',views.getStudentProfiles),
    path('profile/',views.getMyProfile),
    path('document-categories/',views.getDocumentCategories),
    path('document-category/',views.postDocumentCategory),
    path('admin-documents/',views.getStudentDocuments),
    path('admin-verification/',views.verifyDocument),
    path('admin-feedback/',views.commentDocument),
    path('total-users/',views.getTotalUsers),
]
