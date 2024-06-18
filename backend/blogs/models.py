from django.db import models
from django.conf import settings

# Create the author model
class Author(models.Model):
  """Model representing an author."""
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  bio = models.TextField(max_length=400, help_text='Enter your bio details here.')

  def __str__(self):
    """String for representing the Model object."""
    return f"{self.user.first_name} {self.user.last_name}"
  

class Tag(models.Model):
  """ Model representing a blog post tag."""
  name = models.CharField(max_length=200)

  def __str__(self):
    """String for representing the Model object."""
    return self.name
  

class Blog(models.Model):
  """ Model representing a blog post."""
  title = models.CharField(max_length=200)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  content = models.TextField()
  tags = models.ManyToManyField(Tag)
  created_at = models.DateField(auto_now_add=True)

  def __str__(self):
    """String for representing the Model object."""
    return self.title