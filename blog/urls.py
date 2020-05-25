from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='blog'),
    path('<int:blog_id>/', views.post, name='post'),
]
