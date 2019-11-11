from django.urls import path
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('<int:category_id>/<int:article_id>/', ArticleView.as_view()),
    path('<int:category_id>/', CategoryView.as_view()),
    path('', HomeView.as_view())
]

