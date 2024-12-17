from django.db import models

class Posts(models.Model):
    title =  models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f"Title: {self.title} created at {self.created_at}"
