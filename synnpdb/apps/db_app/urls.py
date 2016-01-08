"""urlconf for the base application"""
from django.conf.urls import url, patterns
import views


urlpatterns = patterns(
    '',
    url(r'^pathways/', views.pathways),
    url(r'^autotable/', views.autotable)
)
