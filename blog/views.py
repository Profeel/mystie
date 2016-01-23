#encoding=utf8
from blog.models import BlogPost
from django.template import Context,loader
from django.http.response import HttpResponse
<<<<<<< HEAD
from django.core.context_processors import request
from django.shortcuts import redirect

=======
>>>>>>> parent of ce9f02e... Merge pull request #3 from Profeel/1.0

def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template("archive.html")
    c = Context({'posts':posts})
<<<<<<< HEAD
    return HttpResponse(t.render(c))

def blog(request,blog_id,blog_link=''):
    posts = get_object_or_404(BlogPost, 
                            pk=blog_id, 
                            **admin_criteria(request)
    )
    t = loader.get_template("blog.html")
    c = Context({'posts':posts})
    return HttpResponse(t.render(c))
    #测试ridirect
    #return redirect('/guy')
    return HttpResponse(t.render(c))
=======
    return HttpResponse(t.render(c))
>>>>>>> parent of ce9f02e... Merge pull request #3 from Profeel/1.0
