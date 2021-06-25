from django.db import models
import re
from datetime import datetime

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        TITLE_REGEX = re.compile(r'^[A-Z][a-zA-Z0-9\s]+$')
        if postData['title']:
            if not TITLE_REGEX.match(postData['title']):    
                errors['title'] = "Title must start with a capital letter!"
            elif len(postData['title']) < 2:
                errors['title'] = "The name of the show must be at least 2 characters long"
            elif Show.objects.filter(title=postData['title']) :
                errors['title'] = "Must be a new show"
        if not postData['title']:
            errors['title'] = "Must enter a Title"        
                
        NETWORK_REGEX = re.compile(r'^[A-Z][a-zA-Z0-9\s]+$')
        if postData['title']:
            if not NETWORK_REGEX.match(postData['network']):    
                errors['network'] = "Network must start with a capital letter!"        
            elif len(postData['network']) < 3:
                errors['network'] = "The network of the show must be at least 3 characters long"
        if not postData['network']:
            errors['network'] = "Must enter a Network"

        if postData['date']:
            if datetime.strptime(postData['date'],'%Y-%m-%d') > datetime.now():
                errors['date'] = "Release date must be in the past"
        if not postData['date']:
            errors['date'] = "Must enter a Release date"

        DESC_REGEX = re.compile(r'^[A-Z][a-zA-Z0-9\s]+$')
        if len(postData['description']) != 0: 
            if len(postData['description']) < 10:
                errors['description'] = "The description of the show must be at least 10 characters long"
            if not DESC_REGEX.match(postData['description']):    
                errors['description'] = "Description must start with a capital letter!"
        return errors


class Show(models.Model):
    title = models.CharField(max_length=150)
    network = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()

    def __repr__(self): 
        return f'{self.id} {self.title}'


