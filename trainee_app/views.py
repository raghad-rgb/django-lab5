from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,  get_object_or_404, redirect
from django.views import View 
from django.views.generic import ListView, DetailView, DeleteView
from .models import Trainee
from course_app.models import Track
from .forms import TraineeForm
from django.urls import reverse_lazy
from django.urls import reverse

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})


class TraineeListView(ListView):
     model = Trainee
     template_name = "trainee/trainee_list.html"
     context_object_name = "trainees"

class TraineeDetailView(DetailView):
    model = Trainee
    template_name = "trainee/trainee_detail.html"
    success_url = reverse_lazy('trainee_list')

class AddTrainee(View):
    def get(self, request):
        form = TraineeForm()
        return render(request, "trainee/add_trainee.html", {"form": form})

    def post(self, request):
        form = TraineeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("trainee_list"))
        return render(request, "trainee/add_trainee.html", {"form": form})


class UpdateTrainee(View):
    def get(self, request, trainee_id):
         trainee = get_object_or_404(Trainee, id=trainee_id)
         form = TraineeForm(instance=trainee)
         return render(request, "trainee/update_trainee.html", {"form": form})
    def post(self, request, trainee_id):
         trainee = get_object_or_404(Trainee, id=trainee_id)
         form = TraineeForm(request.POST, request.FILES, instance=trainee)
         if form.is_valid():
            form.save()
            return redirect(reverse("trainee_list"))
         return render(request, "trainee/update_trainee.html", {"form": form})

class TraineeDeleteView(DeleteView):
     model = Trainee
     template_name = "trainee/trainee_confirm_delete.html"
     success_url = reverse_lazy("trainee_list")