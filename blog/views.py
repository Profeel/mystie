from blog.models import BlogPost
from django.template import Context,loader
from django.http.response import HttpResponse

def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template("archive.html")
    c = Context({'posts':posts})
    return HttpResponse(t.render(c))