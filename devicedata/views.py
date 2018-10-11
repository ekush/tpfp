from django.db.migrations import serializer
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def post_data(request):
    if request.method == 'GET':
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
