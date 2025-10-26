from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from tasks.views import TaskViewSet
from users.views import UserViewSet, CurrentUserView

router = DefaultRouter()
router.register('tasks', TaskViewSet, basename='task')
router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/users/me/', CurrentUserView.as_view(), name='current_user'),
    path('api/', include(router.urls)),
]
