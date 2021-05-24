
from django.contrib import admin
from django.urls import path,include
from. import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',views.index, name='main'),
    path('mainnews/',views.news,name='mainnews'),
    path('addnews/',views.addnews,name='addnews'),
    path('mainnews/<int:pk>',views.NewsDetailView.as_view(),name='news-detail'),
    path('mainnews/<int:pk>/update',views.NewsUpdateView.as_view(),name='news-update'),
    path('mainnews/<int:pk>/delete',views.NewsDeleteView.as_view(),name='news-delete'),



] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
