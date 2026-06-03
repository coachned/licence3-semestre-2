from django.db import models
from django.contrib.auth.models import User

class Publication(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    content=models.TextField()
    image=models.ImageField(upload_to='publications', null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} {self.user}"
    
    class Meta:
        verbose_name = "Général"
        verbose_name_plural = "Généraux"

      #  ordering = ["title"]
      

