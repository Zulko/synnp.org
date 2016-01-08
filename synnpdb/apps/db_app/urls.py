"""urlconf for the base application"""

from django.conf.urls import url, patterns, include
import views
urlpatterns = patterns('',
   url(r'^pathways/', views.pathways)
)
