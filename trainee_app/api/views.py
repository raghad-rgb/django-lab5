from rest_framework import generics
from trainee_app.models import Trainee
from .serializers import TraineeSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from trainee_app.api.serializers import TraineeSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class TraineeListCreateView(generics.ListCreateAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer
    parser_classes = (MultiPartParser, FormParser)

@method_decorator(csrf_exempt, name='dispatch')
class UpdateTrainee(generics.UpdateAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer
    lookup_field = 'pk'

class DeleteTrainee(generics.DestroyAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer
