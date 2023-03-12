import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ad, Category

# Create your views here.
from django.views import View


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdView(View):
    def get(self, request):
        ads = Ad.objects.all()
        result = []
        for ad in ads:
            result.append({
                'id': ad.id,
                'name': ad.name,
                'author': ad.author,
                'price': ad.price,
                'description': ad.description,
                'address': ad.address,
                'is_published': ad.is_published,
            })

        return JsonResponse(result, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        new_ad = Ad.objects.create(**data)

        return JsonResponse({
            'id': new_ad.id,
            'name': new_ad.name,
            'author': new_ad.author,
            'description': new_ad.description,
            'address': new_ad.address,
            'is_published': new_ad.is_published,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        result = []
        for category in categories:
            result.append({
                'id': category.id,
                'name': category.name
            })

        return JsonResponse(result, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        # new_category = Category()
        # new_category.name = data['name']
        # new_category.name = data.get("name")
        new_category = Category.objects.create(**data)

        return JsonResponse({
            'id': new_category.id,
            'name': new_category.name,
        })


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwarg):
        ad = self.get_object()
        return JsonResponse({
            'id': ad.id,
            'name': ad.name,
            'author': ad.author,
            'price': ad.price,
            'description': ad.description,
            'address': ad.address,
            'is_published': ad.is_published,
        })


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse({
            'id': category.id,
            'name': category.name
        })
