from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list'),
    path('<int:blog_id>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('add/', views.blog_add, name='blog_add')
]



