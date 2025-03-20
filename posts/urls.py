from django.urls import path
from posts import views


urlpatterns = [
    path("<int:pk>/edit/", views.PostUpdateView.as-viw(), name="edit"),
    path("int:pk>/delete/", views.PostDeleteView.as_view(), name="delete"),
]