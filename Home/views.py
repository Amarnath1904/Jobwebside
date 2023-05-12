from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Jobs, users
import requests
import random
from django.shortcuts import render, redirect
from django.contrib.auth.models import User




def user_login(request):

    
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('password')
        print(username, password)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    return render(request, 'login.html')

def user_signup(request):
    if request.method == 'POST':
        print("1")
        username = request.POST.get('Username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        print("2")
        print(username, password, email)
        try:
            print("3")
            newuser = users.objects.create_user(username, email, password)
            newuser.save()
            print("4")

            return redirect('Home')

        except Exception as e:
            print("====================================")
            print(e)
            return redirect('signup')

    return render(request, 'signup.html')


@login_required(login_url='/signin')
def profile(request, user_id):
    try:
        Userinfo = users.objects.get(id=user_id)
    except:
        Userinfo = User.objects.get(id=user_id)

    if request.method == 'POST':
        print("1")
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        about = request.POST.get('about')
        country = request.POST.get('country')
        street_address = request.POST.get('street-address')
        city = request.POST.get('city')
        state = request.POST.get('region')
        zip = request.POST.get('postal-code')
        resume = request.FILES.get('file-upload')
        profile_pic = request.FILES.get('ProfilePhoto')
        print("2")
        try:
            print("3")
            updateUser = users.objects.get(id=user_id)
            updateUser.About = about
            updateUser.first_name = first_name
            updateUser.last_name = last_name
            updateUser.Country = country
            updateUser.Street_address = street_address
            updateUser.City = city
            updateUser.State = state
            updateUser.Zip = zip

            if resume:
                updateUser.Resume = resume
            elif profile_pic:
                updateUser.ProfilePhoto = profile_pic
            updateUser.save()
            return redirect('profile', user_id=user_id)
        except Exception as e:
            print(e)
            return redirect('profile', user_id=user_id)



    context = {'Userinfo': Userinfo}
    return render(request, 'Profile.html', context)


@login_required(login_url='/signin')
def Home(request):

    user_id = request.user.id

    jobs = Jobs.objects.all()
    context = {'Jobs': jobs,
               "user_id":user_id}



    return render(request, 'index.html', context)


@login_required(login_url='/signin')
def JobProfile(request, id):

    user_id = request.user.id
    job = Jobs.objects.get(Id=id)
    url = f"https://api.unsplash.com/search/photos/?client_id=FpG-xd3S7Y92f_ZsxUIFuOdP1nlOQcBTjHnnqyGEyAE&query={job.JobTitle}&orientation=landscape"
    response = requests.get(url)
    data = response.json()
    num = random.randint(0, len(data)-1)
    url = data['results'][num]['urls']['regular']

    if request.method == 'POST':
        try:
            job = Jobs.objects.get(Id=id)
            job.Applicants.add(request.user)
            return redirect('Home')

    
        except Exception as e:
            print(e)
        
    context = {'Job': job,
               "Image":url,
               "user_id":user_id}
    return render(request, 'job-profile.html', context)

def about(request):
    return render(request, 'about.html')




@login_required(login_url='/signin')
def user_logout(request):
    logout(request)
    return redirect('login')