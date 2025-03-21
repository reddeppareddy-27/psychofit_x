from django.shortcuts import render




def index(request):
    context = {
        "show_banner": request.path not in [
            '/accounts/login/', 
            '/accounts/register/', 
            '/accounts/forgot_password/', 
            '/accounts/reset_password/', 
            '/services/services/', 
            '/privacy-policy/privacy-policy/'
        ]
    }
    return render(request , 'home/index.html' ,context)