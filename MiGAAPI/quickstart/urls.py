from django.conf.urls import url

from . import views #import views


urlpatterns = [
    url(r'species/$', views.matching_species),
]
