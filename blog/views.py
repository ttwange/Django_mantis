from django.shortcuts import render


posts = [  
  {
    "author": "saint",   
    "title": "My first blog post",
    "content":"This is my very first blog post, how exciting!"
  },
  {
    "author": "she",   
    "title": "My second blog post",
    "content":"This is my second blog post, how exciting!"
  }
]


# Create your views here.
def home(request):
  context = {
    'posts': posts  
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html',{"title":"about"})