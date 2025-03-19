from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import course_list, add_course, update_course, delete_course
from course_app.api.views import *


router = SimpleRouter()
router.register(r'track', TrackViewSet, basename='track')

urlpatterns = [
    path('', course_list, name='course_list'),
    path('add/', add_course, name='add_course'),
    path('update/<int:id>/', update_course, name='update_course'),
    path('delete/<int:id>/', delete_course, name='delete_course'),
    path("track/update/<int:pk>/", update_track, name="update_track"),
    path('', include(router.urls)), 
]
