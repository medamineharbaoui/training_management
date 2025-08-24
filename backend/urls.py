# backend/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Views
from workshops.views import AdminWorkshopViewSet, TrainerWorkshopViewSet
from enrollments.views import ParticipantEnrollmentViewSet,  CheckEnrollmentView
from users.views import RegisterView  
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  
from users.views import UserUpdateView, UserListView
from users.views import GetUserByUsernameView



# Swagger / OpenAPI
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# DRF Router
router = DefaultRouter()
router.register(r'admin/workshops', AdminWorkshopViewSet, basename='admin-workshops')
router.register(r'trainer/workshops', TrainerWorkshopViewSet, basename='trainer-workshops')
router.register(r'participant/workshops', ParticipantEnrollmentViewSet, basename='participant-workshops')




#router.register(r'is-enrolled', IsUserEnrolledInWorkshopViewSet, basename='is-enrolled')
# URL Patterns
urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/user/<str:username>/', GetUserByUsernameView.as_view(), name='get_user_by_username'),
    path('api/update/<int:id>/', UserUpdateView.as_view(), name='user-update'),  # admin only
    path('api/admin/users/', UserListView.as_view(), name='admin-user-list'), # admin only
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/workshops/<int:workshop_id>/is-enrolled/', CheckEnrollmentView.as_view(), name='check-enrollment'),



    # API endpoints
    path('api/', include(router.urls)),

    # Swagger / OpenAPI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
