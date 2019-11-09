from django.urls import path
from .views import *

urlpatterns = [
    path('<int:category_id>/<int:article_id>/', ArticleView.as_view()),
    path('<int:category_id>/', CategoryView.as_view()),
    path('', HomeView.as_view())
]

