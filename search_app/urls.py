from django.urls import path
from search_app import views
from . import views
app_name = 'search_app'


urlpatterns = [
    path('',views.SearchResult,name='SearchResult'),
]