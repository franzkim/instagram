from django.conf.urls import url
from . import views

# url namespace
app_name = 'post'
urlpatterns = [
    # /post/$
    url(r'^$', views.post_list, name='post_list'),
    # /post/3/$, /post/35/$
    # 정규표현식에서 매칭된 그룹을 위치인수로 반환하는 방법
    # url(r'^(\d+)/$', views.post_detail),

    # 정규표현식에서 매칭된 그룹을 키워드인수로 반환하는 방법
    # 그룹의 가장 앞 부분에 ?P<패턴이름>을 지정
    url(r'^(?P<post_pk>\d+)/$', views.post_detail, name='post_detail'),
]
