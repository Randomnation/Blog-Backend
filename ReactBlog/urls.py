from django.contrib import admin
from django.urls import path, include
# from django.contrib.auth.models import User
from frontend_main.models import Post, Category
from frontend_main import views, serializers
from rest_framework.routers import DefaultRouter
from rest_framework import viewsets


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserSerializer


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)
# router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include('frontend_main.urls', namespace='frontend-main')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
