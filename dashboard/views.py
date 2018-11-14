from django.shortcuts import render

# Create your views here.


def dashboard_landing_view(request):
    return render(request, 'dashboard/dashboard-landing.html')