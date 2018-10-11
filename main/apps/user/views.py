from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from apps.user.models import *
from django.contrib import messages 
from django.urls import reverse
from random import randint

def register_user(request):
    request.session['data'] = {
        "email": request.POST['email'],
        "firstName": request.POST['firstName'],
        "lastName": request.POST['lastName']
    }
    errors = User.objects.validate(request.POST)
    #registration failure
    if len(errors):
        err_list = ""
        for tag, error in errors.items():
            print(tag, error)
        request.session['data'] = {
            'loginError': "Unable to register. Try Agian."
        }
        return redirect(reverse("hub:home"))
    #registration success
    else:
        this_user = User.objects.register(request.POST)
        request.session.clear()
        request.session['data'] = {
            "id": this_user.id,
            "firstName": this_user.firstName,
            'link': "Log out",
            'logged_in': True
        }
        return redirect(reverse("hub:home"))

def login_user(request):
    user = User.objects.validate_login(request.POST)
    #registration success
    if user:
        request.session['data'] = {
            'id': user.id,
            'firstName': user.firstName,
            'logged_in': True
        }
        return redirect(reverse("hub:home"))
    #registration failure
    else:
        request.session['data'] = {
            'loginEmail': request.POST['loginEmail'],
            'loginError': "Unable to login. Try Agian."
        }
        return redirect(reverse("hub:home"))


def logout(request):
    request.session.clear()
    return redirect(reverse("hub:home"))

def update(request):
    handle_uploaded_file(request.FILES['newimg'], str(request.FILES['newimg']))
    # old_image = loggedinUser.image
    # print(old_image)
    # if(old_image != "noProfile.png"):
    #     _delete_file("/Users/Katiegrace/Source/CD/Django/Airbnb clone/main/media" + old_image)
    this_user = User.objects.get(id=request.session['data']['id'])
    this_user.image = str(request.FILES['newimg'])
    this_user.save()
    return redirect(reverse("hub:profile"))




# ----------------------------- developer tool - fill random data --------------------------------#

def fillusers(request):
    alpha_male = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
    alpha_female = ['p','q','r','s','t','u','v','w','x','y']
    male_first = ['thomas', "Steve", "Juan", "Phillip", "Chuck", "William", "Oliver", "Tommy", "Ben"]
    female_first = ['Jennifer', "Laura", "Maria", "Jada", "Karen", "Holland", "Sophia", "Tina", "Anna"]
    last_name = ["Smith", "Kahn", "Cambell", "Cantu", "Newsome", "Werner", "Pulisic", "Weah", "Trapp", "Acosta", "Brooks", "Zusi", "Guzan", "Miller", "Veracruz", "Judge"]
    for item in alpha_male:
        first = male_first[randint(0, 8)]
        last = last_name[randint(0, 15)]
        email = item + "@" + item + ".com"
        password = item * 4 + "1" * 4
        image1 = "m" + item + ".jpg"
        user1 = {
            'email': email,
            'firstName': first,
            'lastName': last,
            'password': password,
        }
        this_user = User.objects.register(user1)
        this_user.image = image1
        this_user.save()
        
    for item in alpha_female:
        pick = randint(0, 8)
        pick2 = randint(0, 15)
        first = female_first[pick]
        last = last_name[pick2]
        email = item + "@" + item + ".com"
        password = item * 4 + "1" * 4
        image2 = "w" + item + ".jpg"
        user2 = {
            'email': email,
            'firstName': first,
            'lastName': last,
            'password': password,
        }
        this_user = User.objects.register(user2)
        this_user.image = image2
        this_user.save()
    return redirect("hub:profile")