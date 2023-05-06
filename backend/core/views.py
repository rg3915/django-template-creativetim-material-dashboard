from django.shortcuts import render


def index(request):
    template_name = 'index.html'
    context = {}
    return render(request, template_name, context)


def dashboard(request):
    template_name = 'dashboard.html'
    return render(request, template_name)
