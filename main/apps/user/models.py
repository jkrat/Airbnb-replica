from django.db import models
# from datetime import datetime
import re 
import bcrypt 
import os

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate(self, data):
        errors = {}
        #name check
        if len(data['firstName']) < 1:
            errors["firstName"] = "invalid first name"
        #last name check   
        if not data['firstName'].isalpha():
            errors["firstName"] = "invalid first name"
        if len(data['lastName']) < 1:
            errors["lastName"] = "invalid last name"
        #last name check   
        if not data['lastName'].isalpha():
            errors["lastName"] = "invalid last name"
        #email check
        if len(data['email']) < 1 or not EMAIL_REGEX.match(data['email']):
            errors["email"] = "invalid email"
        #duplicate email check
        else:
            duplicate = User.objects.filter(email=data['email'])
            if duplicate:
                errors["email"] = "email already registered"
        #password check
        if len(data['password']) < 8:
            errors["password"] = "invalid password"
        # elif data['password'] != data['confirmPassword']:   
        #     errors["confirmPassword"] = "passwords must match"
        #date check
        # if len(data[dateOfBirth]) < 1:
        #     errors["dateOfBirth"] = "invald date of birth"
        # d = datetime.strptime(day, "%Y-%m-%d")
        # elif d > datetime.now():
        #     errors["dateOfBirth"] = "invald date of birth"
        return errors

    def register(self, data):
        pw = data['password'] 
        hashedpw = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
        hashedpw = (str(hashedpw)).split("'")[1]
        this_user = User.objects.create(firstName=data['firstName'], lastName=data['lastName'], email=data['email'], password=hashedpw)
        return this_user
    
    def validate_login(self, data):
        user = User.objects.filter(email=data['loginEmail'])
        if user:
            this_user = user[0]
            checkAgainst = this_user.password
            if bcrypt.checkpw(data['loginPassword'].encode(), checkAgainst.encode()):
                return this_user
        print("password failed") 
        return False

    # def updateUser(self, data):
    #     User.objects.update(image=data)


class User(models.Model):
    email = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to='media', default='noProfilePic.png')
    objects = UserManager()

def handle_uploaded_file(file, filename):
    with open('media/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def _delete_file(path):
    if os.path.isfile(path):
        os.remove(path)