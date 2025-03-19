from rest_framework import serializers
from course_app.models import Track

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'
