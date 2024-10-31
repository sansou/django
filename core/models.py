from django.db import models

# Create your models here.
class Video(models.Model):
  title = models.CharField(max_length=100, unique=True)
  description = models.TextField()
  thumbnail = models.ImageField(upload_to='media/thumbnails/')
  video = models.FileField(upload_to='media/videos/')
  slug = models.SlugField(max_length=100, unique=True)
  published_at = models.DateTimeField()
  is_published = models.BooleanField(default=False)
  num_likes = models.IntegerField(default=0)
  num_views = models.IntegerField(default=0)
  
  class Meta:
    verbose_name = 'Vídeo'
    verbose_name_plural = 'Vídeos'

  def __str__(self) -> str:
    return self.title