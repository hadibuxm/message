from django.urls import path,include
from .views import CodeListView,BlogCreateView,BlogDetailView
urlpatterns = [
path('post/new/', BlogCreateView.as_view(), name='post_new'), # new
path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), # new
path('', CodeListView.as_view(), name='home'),
]