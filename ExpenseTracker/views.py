from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.http import HttpResponseRedirect
from .email import send_welcome_email

# Create your views here.


def signup_view(request):
   if request.method == 'POST':
       form = SignUpForm(request.POST)
       if form.is_valid():

           form.save()
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password1')

           name = form.cleaned_data['username']
           email = form.cleaned_data['email']

           send_welcome_email(name, email)
           user = authenticate(username=username, password=password)

           login(request, user)

           return redirect('welcome')
   else:
       form = SignUpForm()
   return render(request, 'registration/signup.html', {'form': form})





def profile(request, username):
   current_user = request.user.profile
   user_profile = get_object_or_404(User, username=username)
   profile = Profile.objects.get(user=current_user.user)
   
   if request.method == 'POST':
      user_form = UserUpdateForm(request.POST, instance=request.user)
      profile_form = UserProfileForm(
          request.POST, request.FILES, instance=request.user.profile)
      if user_form.is_valid() and profile_form.is_valid():
          user = user_form.save(commit=False)
          user.profile = profile
          user.profile = request.user.profile
          user.save()

          prof = profile_form.save(commit=False)
          prof.profile = profile
          prof.profile = request.user.profile
          prof.save()

          return HttpResponseRedirect(request.path_info)
   else:
      user_form = UserUpdateForm(instance=request.user)
      profile_form = UserProfileForm(instance=request.user.profile)
   params = {
       'user_form': user_form,
       'profile_form': profile_form,
 
   }
   return render(request , 'expense/profile.html', params)


@login_required
def welcome(request):
   users = User.objects.exclude(id=request.user.id)
   profiles = Profile.objects.all()
   

   params = {
       'users': users,
       'profiles': profiles,
      
   }
   return render(request, 'expense/index.html', params)


