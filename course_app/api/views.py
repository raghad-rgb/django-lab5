from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from course_app.models import Track
from rest_framework import viewsets
from course_app.api.serializers import TrackSerializer

@csrf_exempt  
def update_track(request, pk):
    if request.method == "PATCH":
        try:
            track = Track.objects.get(pk=pk)
            data = json.loads(request.body)

            if "name" in data:
                track.name = data["name"]

            track.save()
            return JsonResponse({"message": "Track updated successfully"}, status=200)

        except Track.DoesNotExist:
            return JsonResponse({"error": "Track not found"}, status=404)
    
    return JsonResponse({"error": "Method not allowed"}, status=405)


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
