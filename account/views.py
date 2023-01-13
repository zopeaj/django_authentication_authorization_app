from django.shortcuts import render
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
# Create your views here.

