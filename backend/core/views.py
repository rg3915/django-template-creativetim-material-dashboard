from django.shortcuts import render


def index(request):
    template_name = 'index.html'
    context = {}
    return render(request, template_name, context)


def dashboard(request):
    template_name = 'dashboard.html'
    return render(request, template_name)


def table(request):
    template_name = 'tables.html'
    return render(request, template_name)


def billing(request):
    template_name = 'billing.html'
    return render(request, template_name)


def notification(request):
    template_name = 'notifications.html'
    return render(request, template_name)


def profile(request):
    template_name = 'profile.html'
    return render(request, template_name)


def signin(request):
    template_name = 'sign-in.html'
    return render(request, template_name)


def signup(request):
    template_name = 'sign-up.html'
    return render(request, template_name)
