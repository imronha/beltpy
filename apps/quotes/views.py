from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Quote
import re
import bcrypt

#----------------- Login/Reg +Validation -------------#
def index(request):
    return render(request, "quotes/index.html")

def register(request):
    errors = User.objects.user_validator(request.POST)
    if len(errors):
        #print error message if fails validation
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/main')
    else:
        #Search the db to see if the user already exists
        found_user = User.objects.filter(email=request.POST['email'])
        if found_user.count() > 0:
            messages.error(request, "Email already taken.", extra_tags="email")
            return redirect('/main')
        else:
            #If the found user doesnt exist, hash their pw and create user object
            hashed_pw = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt())
            new_user = User.objects.create(name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'], password=hashed_pw)
            messages.success(request, 'Successfully registered, you may now log in.')
            return redirect('/main')

def login(request):
    #Check to see if we find any users with the email provided
    found_users = User.objects.filter(email=request.POST['email'])
    if len(found_users) >0:
        #If found, check if their pw matches the hashed pw stored in db
        found_user= found_users.first()
        if bcrypt.checkpw(request.POST['pw'].encode(), found_user.password.encode()) == True:
            #Successfully logged in
            request.session['user_id'] = found_user.id
            request.session['name'] = found_user.name
            print found_user
            return redirect('/quotes')
        else:
            messages.error(request, "Login failed", extra_tags="email")
            return redirect('/main')
    else:
        messages.error(request, "Login failed", extra_tags="email")
        return redirect('/main')
#----------------- End Login/Reg +Validation -------------#

def add_quote(request):
    errors = Quote.objects.quote_validator(request.POST)
    if len(errors):
        # Print error message if fails validation
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/quotes')
    else:
        user = User.objects.get(id=request.session['user_id'])
        quote = Quote.objects.create(author = request.POST['author'], content=request.POST['quote'], added_by_id=request.session['user_id'])
        context = {
            "user": user,
            "all_quotes": Quote.objects.all()
        }
        return render(request, "quotes/home_page.html", context)
def add_fav(request, id):

    pass

def show_user(request,id):
    user = User.objects.get(id=id)
    context = {
        "user": user,
    }
    return render(request, "quotes/show_user.html", context)
def home_page(request):
    quotes = Quote.objects.all().order_by('-created_at')[:3]
    context = {
        "user": User.objects.get(id=request.session['user_id']),
        "all_quotes": Quote.objects.all(),
    }
    return render(request, "quotes/home_page.html", context)
