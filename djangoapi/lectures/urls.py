from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('lecture',views.LectureView)

urlpatterns = [
    path('lec/', include(router.urls) ),
]
