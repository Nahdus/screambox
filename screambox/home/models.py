from django.db import models

# Create your models here.


class Screams(models.Model):
    screamer = models.CharField(max_length=50)
    scream=models.CharField(max_length=250)

    def __str__(self):
        return self.screamer +" :"+"\n"+ self.scream
    
