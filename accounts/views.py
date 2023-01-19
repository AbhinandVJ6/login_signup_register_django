from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

# Create your views here.
def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/login.html')
    return render(request, 'accounts/register.html', {'form': form})

@login_required()
def home(request):
    return render(request,'index.html')

