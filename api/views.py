import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from api.models import Company, User
from api.serializers import CompanySerializer, UserSerializer, SignUpSerializer
from api.serializers.login import LoginSerializer


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GetMe(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    def get(self, request) -> JsonResponse:
        serializer = UserSerializer(request.user)
        return JsonResponse(serializer.data, status=200)


class Login(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SignUpSerializer