from django.urls import include, path

from rest_framework import routers

from .views import PaystackViewSet

router = routers.DefaultRouter()
router.register('payment', PaystackViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
