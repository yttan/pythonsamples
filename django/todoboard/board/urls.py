from django.conf.urls import url

from . import views
app_name = 'board'
urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^(?P<post_user>[a-zA-Z0-9]+)/$', views.postcomment, name='postcomment'),
]
