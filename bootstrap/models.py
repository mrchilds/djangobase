from django.db import models

class ExampleFields(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    def __unicode__(self):
        return self.name
        
class StarWarsCharacter(models.Model):
    name = models.CharField(max_length=200, blank=False)
    def __unicode__(self):
        return self.name