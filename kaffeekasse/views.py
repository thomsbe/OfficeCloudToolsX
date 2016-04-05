from django.shortcuts import render

# Create your views here.
def kaffeekasse(request):
    return render(request, 'index.html')