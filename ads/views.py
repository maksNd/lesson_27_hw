import json

from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from ads.models import Ad, Category

# Create your views here.
from django.views import View

from lesson_27 import settings
from users.models import User


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


class AdListView(ListView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.order_by('-price')

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # ads = self.object_list.all()
        result = []
        for ad in page_obj:
            result.append({
                'id': ad.id,
                'name': ad.name,
                'author_id': str(ad.author_id),
                'price': ad.price,
                'description': ad.description,
                'is_published': ad.is_published,
            })

        return JsonResponse(result, safe=False)


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwarg):
        ad = self.get_object()
        return JsonResponse({
            'id': ad.id,
            'name': ad.name,
            'author': str(ad.author_id),
            'price': ad.price,
            'description': ad.description,
            'is_published': ad.is_published,
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ad
    fields = ['name', 'price', 'description', 'is_published', 'image', 'category_id']

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        author = get_object_or_404(User, pk=data['author_id'])
        category = get_object_or_404(Category, pk=data['category_id'])

        new_ad = Ad.objects.create(
            name=data['name'],
            price=data['price'],
            description=data['description'],
            is_published=data['is_published'],
            author_id=author,
            category_id=category
            # image=data['image'],
        )

        return JsonResponse({
            'id': new_ad.id,
            'name': new_ad.name,
            'author': str(new_ad.author_id),
            'category': str(new_ad.category_id),
            'description': new_ad.description,
            'is_published': new_ad.is_published,
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    model = Ad
    fields = ['name', 'price', 'description', 'is_published', 'image']

    def patch(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        data = json.loads(request.body)
        self.object.name = data['name']
        self.object.price = data['price']
        self.object.description = data['description']
        self.object.is_published = data['is_published']
        # self.object.image = request.FILES['image']
        self.object.save()

        return JsonResponse({
            'id': self.object.id,
            'name': self.object.name,
            'price': self.object.price,
            'description': self.object.description,
            'is_published': self.object.is_published,
            # 'image': self.object.image,
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = Ad
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({'status': 'ok'})


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
