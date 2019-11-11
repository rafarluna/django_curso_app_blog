from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    login_required = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class Article(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    category = models.ForeignKey(Category, related_name='articles', on_delete=models.CASCADE)
    author = models.ForeignKey(Author, related_name='authors', on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.created_datetime)

#python manage.py makemigrations
#python manage.py migrate
