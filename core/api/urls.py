
from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import MyTokenObtainPairView

urlpatterns = [
    path("",views.welcome),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('isloggedin/',views.testAuth),
    path('isadmin/',views.testAuthAdmin),
    path('staff-user/',views.createStaffUser),
    path('student-user/',views.createStudentUser),
    path('student-users/',views.getStudents),
    path('student/',views.deleteStudent),#contains both get and delete
    path('staff-users/',views.getStaffs),
    path('staff/',views.deleteStaff),
    path('change-password/',views.changePassword),
    path('book/',views.createBooking),
    path('booking/',views.bookingView),

]
