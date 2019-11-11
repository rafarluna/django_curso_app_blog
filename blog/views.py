from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .forms import *

from django.template.loader import get_template

class HomeView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        categories = Category.objects.all()
        return render(request, 'home.html', {'articles': articles, 'categories':categories})

class CategoryView(View):

    #@property
    #def category_id(self):
    #    return self.kwargs['category_id']
    
    def get(self, request, category_id=None):
        category = Category.objects.get(id=category_id)
        articles = Article.objects.filter(category=category)
        return render(request, 'category.html', locals())


# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator

class ArticleView(View):

    @property
    def category_id(self):
        return self.kwargs['category_id']

    @property
    def article_id(self):
        return self.kwargs['article_id']
    
    # @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        article = Article.objects.get(id=self.article_id, category_id=self.category_id)
        form = CommentForm()
        return render(request, 'article.html', locals())

    def post(self, request, *args, **kwargs):
        article = Article.objects.get(id=self.article_id, category_id=self.category_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.article = article
            obj.save()
            form = CommentForm()
        return render(request, 'article.html', locals())
