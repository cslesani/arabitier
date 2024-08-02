from django.db import models

# Create your models here.
class Article(models.Model):
    #artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    article_title = models.CharField(max_length=200)
    article_message = models.CharField(max_length=1000)
    article_author = models.CharField(max_length=200)
    article_date=models.DateField()
    article_image = models.ImageField(blank=True,upload_to='article/')