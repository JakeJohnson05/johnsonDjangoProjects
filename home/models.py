from django.db import models
from django.utils import timezone

class JohnsonApp(models.Model):
    """A model that represents an app.
    
    Args:
        appTitle (str): Human friendly title of the app
        appProject (str): 'Real' title of the app
        appPathName (str): the name of the path you want
    
    """
    appTitle = models.CharField(max_length=200)
    appNameSpace = models.CharField(max_length=200)
    
    def __str__(self):
        return self.appTitle
    