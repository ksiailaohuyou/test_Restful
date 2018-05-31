from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
urlpatterns = format_suffix_patterns(urlpatterns)

# 第一二种
# from django.conf.urls import url
# from snippets import  views
# from rest_framework.urlpatterns import format_suffix_patterns
# urlpatterns = [
#     url(r'^snippets/$', views.snippet_list),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
# ]
#
# # 可能有后缀  json,html
# # like:
# # http http://127.0.0.1:8000/snippets/ Accept:application/json  # Request JSON
# # http http://127.0.0.1:8000/snippets/ Accept:text/html         # Request HTML
# # http http://127.0.0.1:8000/snippets.json  # JSON suffix
# # http http://127.0.0.1:8000/snippets.api   # Browsable API suffix
# urlpatterns = format_suffix_patterns(urlpatterns)
