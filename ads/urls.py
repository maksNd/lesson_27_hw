from django.urls import path

from ads import views

urlpatterns = [
    path("ad/", views.AdListView.as_view()),
    path("ad/<int:pk>", views.AdDetailView.as_view()),
    path("ad/create/", views.AdCreateView.as_view()),
    path("ad/update/<int:pk>", views.AdUpdateView.as_view()),
    path("ad/delete/<int:pk>/", views.AdDeleteView.as_view()),

    path("cat/", views.CategoryListView.as_view()),
    path("cat/<int:pk>", views.CategoryDetailView.as_view()),
    path("cat/create/", views.CategoryCreateView.as_view()),
    path("cat/update/<int:pk>", views.CategoryUpdateView.as_view()),
    path("cat/delete/<int:pk>/", views.CategoryDeleteView.as_view()),
]