from django.urls import path

from users import views

urlpatterns = [
    path("", views.UserListView.as_view()),
    path("<int:pk>/", views.UserDetailView.as_view()),
    path("create/", views.UserCreateView.as_view()),
    path("update/<int:pk>", views.UserUpdateView.as_view()),
    path("delete/<int:pk>", views.UserDeleteView.as_view()),

    path("loc/", views.LocationListView.as_view()),

]
