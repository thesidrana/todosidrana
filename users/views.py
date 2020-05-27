from django.shortcuts import render,redirect
#To make validation easier
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm



from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    #Django has classes that turn in to html.
    #We need to specify where to post data after POST request.
    if request.method =="POST":
        form = UserRegisterForm(request.POST) #A new form that has data from above
        if form.is_valid(): # Checks if data is valid eg. Username or password
            form.save() #User created if from is valid
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}. You can now Log In.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})
#Adds functionality that a user must be logged in to view this page
@login_required
def profile(request):
    if request.method =="POST":
        u_form = UserUpdateForm(request.POST,instance = request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance = request.user.profile)
        if u_form.is_valid() and  p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
#Pass on to template
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'users/profile.html',context)
