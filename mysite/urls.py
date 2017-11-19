from django.conf.urls import url, include
from django.contrib import admin

from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'^post/new/$', views.post_new, name='post_new'),
]
