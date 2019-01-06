from django.db import models
from django.core.validators import RegexValidator

class Todo(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    text=models.TextField()
    link_code=models.CharField(max_length=8,unique=True, validators=[alphanumeric])
    title=models.CharField(max_length=40, default="Unknown")
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link_code+" : "+self.text[:20]

