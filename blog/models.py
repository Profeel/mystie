from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    publish_time = models.DateTimeField(auto_now= True)
    body = models.TextField(default='')
    tag = models.ForeignKey('Tag')
    
    class Meta:
        ordering = ['-publish_time']
        
    def __unicode__(self):
        return self.title
    
class Tag(models.Model):
    title = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.title