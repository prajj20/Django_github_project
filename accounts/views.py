from django.shortcuts import render

def login_view(request):
    return render(request, "accounts/login.html")


def signup_view(request):
    return render(request,'accounts/signup.html')

def verify_email_view(request):
    return render(request,'accounts/verify_email.html')

def forgot_pass_view(request):
    return render(request,'accounts/forgot_pass.html')
def reset_pass_view(request):
    return render(request,'accounts/reset_pass.html')