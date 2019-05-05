from django.conf.urls import url, include
from . import views
app_name = 'library'

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logins/$', views.logins, name='logins'),
    url(r'^logintool/$', views.logintool, name='logintool'),
    url(r'^book/$', views.books, name='books'),
    url(r'^book/(\d+)/$', views.book, name='book'),
    url(r'^user/$', views.users, name='users'),
    url(r'^modify/(\d+)/$', views.modify, name='modify'),
    url(r'^judge/$', views.judge, name='judge'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register_tool/$', views.register_tool, name='register_tool'),
    url(r'^query/(\d+)/$', views.query, name='query'),
    url(r'^info/(\d+)/$', views.info, name='info'),
    url(r'^history/(\d+)/$', views.history, name='history'),
    url(r'^reader/(\d+)/$', views.reader, name='reader'),
    url(r'^mod/(\d+)/$', views.mod, name='mod'),
    url(r'^book_info/(\d+)/(\d+)/$', views.book_info, name='book_info'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^ajax/$', views.ajax, name='ajax'),
]
