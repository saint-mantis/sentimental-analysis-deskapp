from django.db import models

class SmModel(models.Model):
    
    inputText = models.CharField(max_length=200)
    
    def __str__(self):
        return self.inputText