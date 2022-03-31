from django.urls import path, include
from .views import RegisterAPI, LoginAPI, UserAPI
from knox import views as knox_views
# from drf_yasg.views import get_schema_view # Commented-out line as it
# was not in use
# from drf_yasg import openapi # Commented-out line of code as it was 
# not in use
from rest_framework import permissions

# BUG:
##### BELOW PIECE OF CODE IS COMMENTED-OUT BECAUSE drf_yasg SWAGGER WAS
##### NOT LETTING TO DEPLOY THE APPLICATION ON HEROKU

# schema_view = get_schema_view(
#    openapi.Info(
#       title="Backend Developer Trial Assignment Login/Logout API",
#       default_version='v1',
#       description="This is the API for Meistry Global Teams' Backend\
#            Developer Trial Assignment, where a use can create \
#                account, log in and enter personal details with a CSV\
#                     file.",
#       terms_of_service="#",
#       contact=openapi.Contact(email="khubikhawar@gmail.com"),
#       license=openapi.License(name="Khubaib Khawar"),
#    ),
#    public=True,
#    permission_classes=[permissions.AllowAny],
# )

##### COMMENTED-OUT CODE ENDS HERE

urlpatterns = [
    path('api/v1/', include('knox.urls')),
    path('api/v1/register', RegisterAPI.as_view()),
    path('api/v1/login', LoginAPI.as_view()),
    path('api/v1/user', UserAPI.as_view()),
    path(
        'api/v1/logout',
        knox_views.LogoutView.as_view(),
        name="logout"
    ),
]