from django.conf.urls import url
from django.contrib import admin

from django.conf.urls import url, include
from .api import views
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from rest_framework.schemas import get_schema_view


router = DefaultRouter()
router.register(r'spots', views.SpotViewSet)


# localhost:8000/spec/ui/?format=openapi

urlpatterns = [
	url(r'^', include(router.urls)),
	url('^spots/tagged/(?P<tag_name>.+)$', views.SpotTagsView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^spec/ui/', get_swagger_view(title='API')),
]
