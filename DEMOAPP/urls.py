from django.urls import path
from . import views
from django.conf.urls import url
#from .views import PostListView, PostDetailView

urlpatterns = [
#    path('', PostListView.as_view(), name='home-page'),
#    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('', views.home, name='home-page'),
    path('about/', views.about, name='about-page'),
    path('upload/', views.upload, name='upload-page'),
    url('predictMusic',views.predictMusic,name='predictMusic'),
]