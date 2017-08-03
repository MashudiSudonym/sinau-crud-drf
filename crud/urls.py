from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = {
    url(r'^$', views.CrudList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.CrudDetail.as_view()),
}

urlpatterns = format_suffix_patterns(urlpatterns)
