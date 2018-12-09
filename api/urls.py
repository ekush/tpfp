"""
@author: Rashedul Kabir
Created on: 12/9/18
"""

from django.conf.urls import url

from devicedata.views import post_data

urlpatterns = [
    url(r'^post', post_data),
]
