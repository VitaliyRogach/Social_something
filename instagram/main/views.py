from django.shortcuts import render

# Create your views here.


def singview(request):
    return render(request, 'main/sing.html')
