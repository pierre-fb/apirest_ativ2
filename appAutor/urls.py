from appAutor.views import autor_list
from django.urls import path

urlpatterns = [
    path('',autor_list),
]