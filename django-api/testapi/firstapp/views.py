from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.


class TestApi(APIView):

    def get(self, request):
        return Response(data={"message":"This is a django test api."}, status=status.HTTP_200_OK)
    
    def post(self, request):

        return Response(data={"name":request.data.get("name","NA")}, status=status.HTTP_200_OK)
