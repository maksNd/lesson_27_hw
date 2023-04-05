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

from ads.serializers import AdSerializer, SelectionSerializer, SelectionCreateSerializer, AdCreateSerializer


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


@method_decorator(csrf_exempt, name='dispatch')
class CategoryListView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        categories = self.object_list.order_by('name')
        result = []
        for category in categories:
            result.append({
                'id': category.id,
                'name': category.name
            })

        return JsonResponse(result, safe=False)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse({
            'id': category.id,
            'name': category.name
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryCreateView(CreateView):
    model = Category

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        new_category = Category.objects.create(**data)

        return JsonResponse({
            'id': new_category.id,
            'name': new_category.name,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']

    def patch(self, request, *args, **kwargs):
        print('ok')
        print(args)
        print(kwargs)
        super().get(request, *args, **kwargs)

        data = json.loads(request.body)

        self.object.name = data['name']
        self.object.save()

        return JsonResponse({
            'id': self.object.id,
            'name': self.object.name,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({'status': 'ok'})


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
