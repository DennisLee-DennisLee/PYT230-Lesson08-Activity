from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from rest_framework import routers
from blogging.views import UserViewSet, GroupViewSet, PostViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('polling/', include('polling.urls')),
    path('admin/', admin.site.urls),
    # path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    # path('logout/', LogoutView.as_view(next_page='/'), name="logout"),
]
