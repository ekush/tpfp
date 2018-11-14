from django.conf.urls import url

from .views import dashboard_landing_view


urlpatterns = [
    url(r'^$', dashboard_landing_view),
]
