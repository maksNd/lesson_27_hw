from django.urls import path
from rest_framework import routers

from ads import views

router = routers.SimpleRouter()
router.register("selection", views.SelectionViewSet)
router.register("ad", views.AdViewSet)

urlpatterns = [

    path("cat/", views.CategoryListView.as_view()),
    path("cat/<int:pk>", views.CategoryDetailView.as_view()),
    path("cat/create/", views.CategoryCreateView.as_view()),
    path("cat/update/<int:pk>", views.CategoryUpdateView.as_view()),
    path("cat/delete/<int:pk>/", views.CategoryDeleteView.as_view()),

]

urlpatterns += router.urls
