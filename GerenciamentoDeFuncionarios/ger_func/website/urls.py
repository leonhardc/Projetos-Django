from django.urls import path
from . import views

app_name = 'website'

# urlpatterns contem a lista de reteamento de URLs
urlpatterns = [
    path('', views.index, name='index')
]
