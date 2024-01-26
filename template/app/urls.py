from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view
router = DefaultRouter()


@api_view(['GET'])
def test(request):
    return Response('Hello, World!')


urlpatterns = [
    path('test', test),
]
