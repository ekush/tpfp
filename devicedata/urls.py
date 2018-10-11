from django.conf.urls import url

from .views import post_data

urlpatterns = [
    url(r'^post/', post_data),
]
