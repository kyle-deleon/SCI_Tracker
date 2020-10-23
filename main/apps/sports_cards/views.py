from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    return render(request, 'index.htm')

def create_users(request):
    errors = User.objects.validator(request.POST)
    #connects to models.py def validator through class User.objects
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            first_name=request.POST["first_name"], 
            last_name=request.POST["last_name"], 
            user_name=request.POST["user_name"],
            email=request.POST["email"],  
            password=hash_pw 
            )
        print(user)
        request.session['uid'] = user.id
        #request.session['greeting'] = request.POST["first_name"]

        return redirect("/dashboard")

def login(request):
    # see if the username provided exists in the database
    user = User.objects.filter(email=request.POST['email']) # why are we using filter here instead of get?
    if len(user) > 0: # note that we take advantage of truthiness here: an empty list will return falsecopy
        logged_user = user[0] 
        # assuming we only have one user with this username, the user would be first in the list we get back
        # of course, we should have some logic to prevent duplicates of usernames when we create users
        # use bcrypt's check_password_hash method, passing the hash from our database and the password from the form
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            # if we get True after checking the password, we may put the user id in session
            request.session['uid'] = logged_user.id
            # never render on a post, always redirect!
            return redirect('/dashboard')
        else:
            messages.error(request, "Email and password did not match.")
    # if we didn't find anything in the database by searching by username or if the passwords don't match, 
    # redirect back to a safe route
    else:
        messages.error(request, "Email address is not registered.")

    return redirect("/")

def dashboard(request):
    context = {
        "logged_user": User.objects.get(id=request.session['uid']),
        "all_cards": Cards.objects.all().order_by("-created_at")
    }
    return render(request, "dashboard.htm", context)

def new_card(request):
    return render (request, "new.htm")

def create_card(request):
    errors = Cards.objects.validator(request.POST)

def logout(request):
    request.session.flush()

    return redirect('/')