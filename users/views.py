# Create your views here.
# users/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

# users/views.py


class CustomLoginView(LoginView):
    template_name = 'users/login.html'

@login_required
def profile_view(request):
    return render(request, 'users/profile.html', {})


