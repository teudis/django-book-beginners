from posts.models import Post
from django.shortcuts import render
from django.views.generic import ListView

from .models import Post

# Create your views here.
class HomePageView(ListView):
        template_name = 'home.html'
        model = Post
        context_object_name = "all_post"