from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [

    path('', views.user_list.as_view()),
    path('register', views.register_user.as_view()),
    path('<int:pk>', views.user_detail.as_view()),
    path('token', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()), 
    path('forgot_password', views.forgot_password.as_view()),
]
