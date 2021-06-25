from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "The name of the show must be at least 2 characters long";
        
        if len(postData['network']) < 3:
            errors['network'] = "The network of the show must be at least 3 characters long";
        if len(postData['description']) != 0: 
            if len(postData['description']) < 10:
                errors['description'] = "The description of the show must be at least 10 characters long";
        
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


