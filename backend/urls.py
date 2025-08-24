# backend/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Views
from workshops.views import AdminWorkshopViewSet, TrainerWorkshopViewSet
from enrollments.views import ParticipantEnrollmentViewSet
from users.views import RegisterView  
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  
from users.views import UserUpdateView, UserListView


# Swagger / OpenAPI
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# DRF Router
router = DefaultRouter()
router.register(r'admin/workshops', AdminWorkshopViewSet, basename='admin-workshops')
router.register(r'trainer/workshops', TrainerWorkshopViewSet, basename='trainer-workshops')
router.register(r'participant/workshops', ParticipantEnrollmentViewSet, basename='participant-workshops')

# URL Patterns
urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/update/<int:id>/', UserUpdateView.as_view(), name='user-update'),  # admin only
    path('api/users/', UserListView.as_view(), name='admin-user-list'), # admin only
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API endpoints
    path('api/', include(router.urls)),

    # Swagger / OpenAPI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
