import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from ads.models import Ad, Category, Selection
from ads.permissions import IsOwner, IsStaff

from ads.serializers import AdSerializer, SelectionSerializer, SelectionCreateSerializer, AdCreateSerializer, \
    CategorySerializer


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


class AdViewSet(ModelViewSet):
    queryset = Ad.objects.all()
    default_serializer_class = AdSerializer

    default_permission = [AllowAny]
    permissions = {
        'retrieve': [IsAuthenticated],
        'update': [IsAuthenticated, IsOwner | IsStaff],
        'partial_update': [IsAuthenticated, IsOwner | IsStaff],
        'destroy': [IsAuthenticated, IsOwner | IsStaff],
    }

    serializers = {
        'list': AdSerializer,
        'create': AdCreateSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer_class)

    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]


class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SelectionViewSet(ModelViewSet):
    queryset = Selection.objects.all()
    default_serializer_class = SelectionSerializer

    default_permission = [AllowAny]
    permissions = {
        'retrieve': [IsAuthenticated],
        'create': [IsAuthenticated],
        'update': [IsAuthenticated, IsOwner],
        'partial_update': [IsAuthenticated, IsOwner],
        'destroy': [IsAuthenticated, IsOwner],
    }

    serializers = {
        'list': SelectionSerializer,
        'create': SelectionCreateSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer_class)

    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]
