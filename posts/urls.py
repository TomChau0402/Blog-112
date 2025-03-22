from django.urls import path
from posts import views


urlpatterns = [
   
    path("", views.PostListView.as_view(), name="list"),
    path("drafts/", views.DrafPostListView.as_view(), name="drafts"),
    path("archived/", views.ArchivedPostView.as_view(), name="archive"),
    path("new/", views.PostCreateView.as_view(), name="new"),
    path("int:pk>", views.PostDetailView.as_view(), name="detail"),
    path("int:pk>/delete/", views.PostDeleteView.as_view(), name="delete"),
    path("<int:pk>/edit/", views.PostUpdateView.as-viw(), name="edit"),
    ]