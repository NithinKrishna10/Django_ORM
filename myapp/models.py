from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField(default=0)
    bio = models.TextField()
    # class Meta:
    #     ordering = ['-name'] 
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
# Types of model inheritance in Django
class BaseModel(models.Model):
    # Fields shared by all models
    class Meta:
        abstract = True

class SubModel(BaseModel):
    # Additional fields specific to the sub-model
    data = models.CharField(max_length=200)


@receiver(post_save, sender=Post)
def post_saved(sender, instance, created, **kwargs):
    if created:
        # Do something when a post is saved
        print('hai')

# Raw method
