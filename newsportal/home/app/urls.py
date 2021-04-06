from .views import *
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

app_name = 'app'

urlpatterns = [
    path('', homeView, name='home'),
    path('category/', category, name='category'),
    path('about/', aboutView, name='about'),
    path('latest/', latestView, name='latest'),
    path('contact/', contactView, name='about'),
    path('element/', elementView, name='element'),
    path('blog/', blogView, name='blog'),
    path('single/', singleView, name='single'),
    path('details/', detailsView, name='details'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
