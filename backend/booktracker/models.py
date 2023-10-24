from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name
    
    # title, description, read(bool), author
class Book(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    read = models.BooleanField(default=False)
    author = models.ForeignKey(
                Author, on_delete=models.CASCADE)

    # RENAME THE INSTANCE OF YOUR MODEL
    def _str_(self):
        return self.title