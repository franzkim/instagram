from django.conf.urls import include
from django.conf.urls import url

urlpatterns = [
    url(r'^post/', include('post.urls.urls_apis')),
]
