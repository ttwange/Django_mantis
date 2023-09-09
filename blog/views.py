from django.shortcuts import render


post = [
  {
    "author": "saint"   
    "title": "My first blog post",
    "content":"This is my very first blog post, how exciting!"
  },
  {
    "author": "saint"   
    "title": "My first blog post",
    "content":"This is my very first blog post, how exciting!"
  }
]


# Create your views here.
def home(request):
  return render(request, 'blog/home.html')

def about(request):
  return render(request, 'blog/about.html')