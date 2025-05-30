from django.urls import path
from api.views import Userregister
from rest_framework.routers import DefaultRouter
from api.views import Todomodelviewset

from rest_framework.authtoken.views import ObtainAuthToken

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router=DefaultRouter()
# router used because of viewset
# router.register('todos',Todoviewsetview,basename='api')
router.register('todomodelview',Todomodelviewset,basename='api')

urlpatterns=[
   #  path('register/',Userregister.as_view(),name='register'),
    path('token/',ObtainAuthToken.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]+router.urls