from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class Screams(models.Model):
    screamer = models.CharField(max_length=50)
    scream=models.CharField(max_length=250,null=True)


    def get_absolute_url(self):
        return reverse('home:screams', kwargs={'pk':self.pk})

    def __str__(self):
        return "screamer"+ str(self.screamer) +" :"+"\n"+ "scream"+ str(self.scream)
    
