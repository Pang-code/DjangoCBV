"""DjangoCBV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from book import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('version/', views.version),
    path('books/', views.book),
    path('book/', views.BookView.as_view()),
    path('bookAPIview/', views.BookAPIView.as_view()),
    path('bookview/', views.BookViewToModels.as_view()),
    re_path('bookview/(\d+)', views.BookDetailViewToModels.as_view()),
    path('bookview2/', views.BookViewToModelsGenericAPIView.as_view()),
    path('publish/', views.PublishViewToModelsGenericAPIView.as_view()),
    re_path('publish/(?P<pk>\d+)', views.PublishDetailViewToModelsGenericAPIView.as_view()),
    path('author/', views.AuthorViewToModelsGenericAPIView.as_view()),
    re_path('author/(?P<pk>\d+)', views.AuthorDetailViewToModelsGenericAPIView.as_view()),

]