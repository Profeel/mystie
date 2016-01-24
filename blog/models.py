from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    publish_time = models.DateTimeField(auto_now= True)
    body = models.TextField(default='')
    tag = models.ForeignKey('Tag')
    
    class Meta:
        ordering = ['-publish_time']
    
    def save(self, *args, **kwargs):
        self.link = slugify(self.link)
        self.snippet = self.content[:321]
        super(BlogPost, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('BlogPost:BlogPost', args=(self.id,self.link))

class Tag(models.Model):
    title = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.title