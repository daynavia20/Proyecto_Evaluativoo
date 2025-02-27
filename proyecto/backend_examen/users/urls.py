from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('sign_up/', views.signUpView.as_view(), name='sign_up'),
    path('edit_user/<int:pk>/', views.editUserView.as_view(), name='edit_user'),
    path('detail_user/<int:pk>/', views.detailUserView.as_view(), name='detail_user'),
    path('list_user/', views.listUserView.as_view(), name='list_user'),
    path('login/', views.loginView.as_view(), name='login'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]