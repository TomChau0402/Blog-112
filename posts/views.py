from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Post
from django.urls import reverse_lazy


class PostUpdateView(UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = [
        "title", "subtitle", "body", "status"
    ]

class PostCreateView(CreateViewView):
    template_name = "posts/edit.html"
    model = Post
    fields = [
        "title", "subtitle", "body", "status"
    ]

class PostListView(ListViewView):
    template_name = "posts/edit.html"
    model = Post
    fields = [
        "title", "subtitle", "body", "status"
    ]

class PostDeleteView(deleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("list")
    
