from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views, classbased_views

#urlpatterns = [
#    url(r'^$', views.snippet_list),
#    url(r'(?P<pk>[0-9]+)/$', views.snippet_detail),
#]

#urlpatterns = [
#    url(r'^$', classbased_views.SnippetList.as_view()),
#    url(r'(?P<pk>[0-9]+)/$', classbased_views.SnippetDetail.as_view()),
#    url(r'^users/$', classbased_views.UserList.as_view()),
#    url(r'users/(?P<pk>[0-9]+)/$', classbased_views.UserDetail.as_view()),
#]


#urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns = format_suffix_patterns([
        url(r'^api/$', 
            classbased_views.api_root),
        url(r'^$', 
            classbased_views.SnippetList.as_view(), 
            name = 'snippet-list'),
        url(r'(?P<pk>[0-9]+)/$', 
            classbased_views.SnippetDetail.as_view(), 
            name = 'snippet-detail'),
        url(r'^users/$', 
            classbased_views.UserList.as_view(), 
            name = 'user-list'),
        url(r'users/(?P<pk>[0-9]+)/$', 
            classbased_views.UserDetail.as_view(), 
            name = 'user-detail'),
])

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
]
