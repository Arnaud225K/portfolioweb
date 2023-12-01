from django.shortcuts import render, redirect, get_object_or_404



def home(request):
    return render(request,'portfolio/home.html')


def service_detail(request):
    return render(request, 'portfolio/includes/service/service-detail.html')

def handler400(request,exception):
    return render(request, '400.html')

def handler403(request,exception):
    return render(request, '403.html')

def handler404(request,exception):
    return render(request, '404.html')

def handler500(request):
    return render(request, '500.html')