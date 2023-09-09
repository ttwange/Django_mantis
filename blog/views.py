from django.shortcuts import render
from .models import Post

posts = [  
  {
    "author": "saint",   
    "title": "My first blog post",
    "content":"This is my very first blog post, how exciting!",
    "date_posted":"September 9, 2023"
  },
  {
    "author": "she",   
    "title": "My second blog post",
    "content":"This is my second blog post, how exciting!",
    "date_posted":"September 9, 2023"
  }
]


# Create your views here.
def home(request):
  context = {
    'posts': Post.objects.all()  
  }
  return render(request, 'blog/home.html', context)

def about(request):
  context = {"title":"About"}
  return render(request, 'blog/about.html',context)