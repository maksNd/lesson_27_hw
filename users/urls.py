from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users import views
from users.views import LocationViewSet

router = routers.SimpleRouter()
router.register('location', LocationViewSet)

urlpatterns = [
    path("", views.UserListView.as_view()),
    path("<int:pk>/", views.UserDetailView.as_view()),
    path("create/", views.UserCreateView.as_view()),
    path("update/<int:pk>", views.UserUpdateView.as_view()),
    path("delete/<int:pk>", views.UserDeleteView.as_view()),
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),

    # path("loc/", views.LocationListView.as_view()),
]

urlpatterns += router.urls
