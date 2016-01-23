from blog.models import BlogPost
from django.template import Context,loader
from django.http.response import HttpResponse
from django.core.context_processors import request

def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template("archive.html")
    c = Context({'posts':posts})
    return HttpResponse(t.render(c))

def blog(request):
    posts = BlogPost.objects.all()
    t = loader.get_template("blog.html")
    c = Context({'posts':posts})
    return HttpResponse(t.render(c))