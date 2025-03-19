from django.urls import path, include
from .views import TraineeListView, TraineeDetailView, TraineeDeleteView, AddTrainee, UpdateTrainee, register
from trainee_app.api.views import *


urlpatterns = [
    path("", TraineeListView.as_view(), name="trainee_list"),
    path("add/", AddTrainee.as_view(), name="add_trainee"),
    path("trainee/<int:pk>/", TraineeDetailView.as_view(), name="trainee_detail"),
    path('update/<int:pk>/', UpdateTrainee.as_view(), name='update_trainee'),
    path('delete/<int:pk>/', DeleteTrainee.as_view(), name='delete_trainee'),
    path('register/', register, name='register'),
    path('trainees/', TraineeListCreateView.as_view(), name='trainee-list-create'),
]
