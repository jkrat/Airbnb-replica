from django.shortcuts import render, redirect
from apps.user.models import *
from django.contrib import messages 
from django.urls import reverse

def profile(request):
    return redirect("hub:home") 

# def check_login_status(request):
#     if 'user_id' not in request.session:
        # return   

def register_user(request):
    request.session['data'] = {
        "email": request.POST['email'],
        "firstName": request.POST['firstName'],
        "lastName": request.POST['lastName'],
        # "dob": request.POST['dateOfBirth'],
    }
    errors = User.objects.validate(request.POST)
    #registration failure
    if len(errors):
        for tag, error in errors.items():
            print(tag, error)
            messages.error(request, error, extra_tags=tag)
        return redirect(reverse("hub:home"))
        #registration success
    else:
        User.objects.register(request.POST)
        request.session.clear()
        id = User.objects.get(email=request.POST['email']).id
        request.session['data'] = {
            "id": id,
            "firstName": request.POST['firstName'],
            'logged_in': True
        }
        return redirect(reverse("hub:home"))

def login_user(request):
    user = User.objects.validate_login(request.POST)
    if user:
        firstName =User.objects.get(id=user).firstName
        request.session['data'] = {
            'id': user,
            'firstName': firstName,
            'logged_in': True
        }
        print("logged in: ", request.session['data'])
        print(request.session['data']['id'])
        return redirect(reverse("hub:home"))
    else:
        request.session['data'] = {
            'loginEmail': request.POST['loginEmail'],
            'loginError': "unable to login"
        }
        return redirect(reverse("hub:home"))

# def access_wall(request):
#     if 'data' in request.session:
#         context = {
#             "friends": User.objects.filter(relationships__id=request.session['data']['id']).exclude(id=request.session['data']['id']),
#             "nonFriends": User.objects.all().exclude(relationships__id=request.session['data']['id']).exclude(id=request.session['data']['id'])
#         }
#         print(context)
#         return render(request, "belt/wall.html", context)
#     return redirect("home")

# def display_user(request, user_id): 
#     context = {
#         "user": User.objects.get(id=user_id)
#     }
#     return redirect(" hub:profile")

# def add(request, user_id):
#     Relationship.objects.create(from_user_id=user_id, to_user_id=request.session['data']['id'])
#     Relationship.objects.create(from_user_id=request.session['data']['id'], to_user_id=user_id)


#     return redirect("wall")

# def remove(request, user_id): 
#     Relationship.objects.filter(from_user_id=user_id, to_user_id=request.session['data']['id']).delete()
#     Relationship.objects.filter(from_user_id=request.session['data']['id'], to_user_id=user_id).delete()
#     return redirect("wall")

def logout(request):
    request.session.clear()
    print("\n\n")
    print("--------------- loggedout -------------")
    print("\n\n")
    return redirect(reverse("hub:home"))

def update(request):
    handle_uploaded_file(request.FILES['newimg'], str(request.FILES['newimg']))
    loggedinUser = User.objects.get(id=request.session['data']['id'])
    loggedinUser.image = str(request.FILES['newimg'])
    loggedinUser.save()
    return redirect(reverse("hub:profile"))
