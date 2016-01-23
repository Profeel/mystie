#encoding=utf-8
from django.db import models
from django.core.urlresolvers import reverse

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    publish_time = models.DateTimeField(auto_now= True)
    link = models.CharField(u'链接', max_length=150, default='')
    link.help_text = u"Cool URIs don't change"
    content = models.TextField(default='')
    snippet = models.CharField(u'摘要', max_length=500, default='') 
    tag = models.ForeignKey('Tag')
    
    class Meta:
        ordering = ['-publish_time']
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('BlogPost:BlogPost', args=(self.id,self.link))
    
class Tag(models.Model):
    title = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.title