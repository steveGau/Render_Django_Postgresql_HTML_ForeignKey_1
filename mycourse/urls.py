from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name="mycourse"

urlpatterns = [
    path('', views.home, name="homepage"),
]

#   path('all_tables/', views.all_tables, name='all_tables'),