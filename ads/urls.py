from django.urls import path
from rest_framework import routers

from ads import views

router = routers.SimpleRouter()
router.register("selection", views.SelectionViewSet)
router.register("ad", views.AdViewSet)
router.register("cat", views.CategoryViewset)

urlpatterns = []

urlpatterns += router.urls
