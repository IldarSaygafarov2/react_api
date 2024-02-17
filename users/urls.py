from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path('login', views.MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('register', views.RegisterView.as_view(), name='auth_register'),
    path('users/<int:pk>/update', views.UserUpdateView.as_view()),
    path('users/<int:pk>/update/avatar', views.UserAvatarUpdateView.as_view()),
    path('users/profile', views.get_profile)
]
