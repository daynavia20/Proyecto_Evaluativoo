from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateBlogView.as_view()),
    path('list/', views.ListBlogView.as_view()),
    path('edit/<int:pk>/', views.EditBlogView.as_view()),
    path('delete/<int:pk>/', views.DeleteBlogView.as_view()),
    path('comentario/', views.ComenatarioView.as_view()),
    path('comentario_list/', views.ListComentarioView.as_view()),
]
