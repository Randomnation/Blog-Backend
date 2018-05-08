from django.urls import path, re_path
from frontend_main import views
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'frontend_main'

urlpatterns = [
    path('', views.post_list, name='index'),
    path('post/', views.PostList.as_view(), name="post-list"),
    re_path(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name="post-detail"),
    path('category/', views.CategoryList.as_view(), name="category-list"),
    re_path(r'^category/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view(), name="category-detail"),
    path('user/', views.UserList.as_view(), name="user-list"),
    re_path(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name="user-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
