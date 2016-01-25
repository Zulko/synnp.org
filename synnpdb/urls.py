"""synnpdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
import synnpdb.views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from registration.backends.simple.views import RegistrationView
import synnpdb
admin.autodiscover()


class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return '/'


urlpatterns = [
    url(r'', include('synnpdb.apps.db_app.urls')),
    url(r'^$', synnpdb.views.index, name='index'),
    url(r'^about/', synnpdb.views.about, name='about'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(),
        name='registration_register'),
    url(r'^db_view/', synnpdb.views.db_view, name='db_view'),
    url(r'^plate/', include('django_spaghetti.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
    #url(r'^tinymce/', include('tinymce.urls')),

    url(
        r'^favicon.ico$',
        RedirectView.as_view(
            url=staticfiles_storage.url('favicon.ico'),
            permanent=False),
        name="favicon"
    )
]
