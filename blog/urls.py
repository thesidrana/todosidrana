from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('',PostListView.as_view(), name='blog-home'), #  name is used later for href links
    #Unique Pages
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('about/',views.about, name='blog-about'),
    path('cal/',views.cal,name='blog-calendar')
]
#Path for home page. Uses function home from views.py to send Http req
#Recieves string which empty and is mapped to '' and views.home
