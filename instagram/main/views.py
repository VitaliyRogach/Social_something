from django.shortcuts import render

# Create your views here.


def signview(request):
    return render(request, 'main/sign.html')

def registration(request):

    return render(request, 'main/registration.html')

def main_page(request):
    return render(request, 'main/main.html')