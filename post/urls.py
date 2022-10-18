from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('',views.PostApiView.as_view(), name="post"),
    path('<int:pk>/', views.PostDetailApiView.as_view(), name="post_detail"),
    
    ]