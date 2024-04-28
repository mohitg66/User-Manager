from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )

    gender = models.CharField(max_length=1, choices=gender_choices)
    skills = models.ManyToManyField('Skill', related_name='users', blank=True)
    
    def get_skills(self):
        return ', '.join([skill.name for skill in self.skills.all()])
        
    def __str__(self):
        return self.username
    
class Skill(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    
    def __str__(self):
        return self.name