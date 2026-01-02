from django.urls import path
from .views import login_view ,signup_view,verify_email_view,forgot_pass_view,reset_pass_view

urlpatterns = [
    path('login/', login_view, name="login"),
    path('signup/',signup_view,name="signup"),
    path('verifyemail/',verify_email_view,name="verifyemail"),
    path('forgotpass/',forgot_pass_view,name="forgotpass"),
    path('resetpass/',reset_pass_view,name="resetpass"),
    
]
