from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views, classbased_views

#urlpatterns = [
#    url(r'^$', views.snippet_list),
#    url(r'(?P<pk>[0-9]+)/$', views.snippet_detail),
#]

urlpatterns = [
    url(r'^$', classbased_views.SnippetList.as_view()),
    url(r'(?P<pk>[0-9]+)/$', classbased_views.SnippetDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
