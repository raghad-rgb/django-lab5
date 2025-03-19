from django import forms
from .models import Trainee
from course_app.models import Track

class TraineeForm(forms.ModelForm):
    class Meta:
        model = Trainee
        fields = ['name', 'email', 'creation_date', 'image', 'track']

    track = forms.ModelChoiceField(
        queryset=Track.objects.all(),
        empty_label="-- Select Track --",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
