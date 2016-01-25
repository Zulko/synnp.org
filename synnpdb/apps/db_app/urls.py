"""urlconf for the base application"""
from django.conf.urls import url, patterns
import views


urlpatterns = patterns(
    '',
    url(r'^parts/', views.parts),
    url(r'^compounds/', views.compounds),
    url(r'^autotable/', views.autotable),
    url(r'^demo_spreadsheet/', views.demo_spreadsheet),
    url(r'^display_object/', views.display_object),
    url(r'^demo_form/', views.demo_form)
)
