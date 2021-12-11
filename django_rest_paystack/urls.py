from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="Pastebin API")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/paystack/", include("paystack.urls")),
    path("docs/", schema_view),
]
