from django.urls import path
from . import views
from .views import AddCommit

urlpatterns = [
    path('', views.PostView.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('comment/<int:pk>/', AddCommit.as_view(), name='comment')
]

