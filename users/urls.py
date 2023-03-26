from django.urls import path
from rest_framework import routers

from users import views
from users.views import LocationViewSet

router = routers.SimpleRouter()
router.register('loc', LocationViewSet)

urlpatterns = [
    path("", views.UserListView.as_view()),
    path("<int:pk>/", views.UserDetailView.as_view()),
    path("create/", views.UserCreateView.as_view()),
    path("update/<int:pk>", views.UserUpdateView.as_view()),
    path("delete/<int:pk>", views.UserDeleteView.as_view()),

    # path("loc/", views.LocationListView.as_view()),

]

urlpatterns += router.urls
