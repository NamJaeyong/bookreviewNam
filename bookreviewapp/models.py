from django.db import models
from django.utils import timezone

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=200)    
    contents = models.TextField()
    price = models.CharField(max_length=100)
    score = models.CharField(choices=(('ㅆㅎㅌㅊ', ("ㅆㅎㅌㅊ")),
                                        ('ㅎㅌㅊ', ("ㅎㅌㅊ")),
                                        ('ㅍㅌㅊ', ("ㅍㅌㅊ")),
                                        ('ㅅㅌㅊ', ("ㅅㅌㅊ")),
                                        ('ㅆㅅㅌㅊ', ("ㅆㅅㅌㅊ"))),
                                        max_length = 50)
    img = models.FileField(null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title 

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField() 

