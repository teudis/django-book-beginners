from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy # new

from .models import Post
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "all_posts"


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class BlogCreateView(CreateView):
    model =  Post
    template_name = "post_new.html"
    fields= ['title', 'body', 'author']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy('home')