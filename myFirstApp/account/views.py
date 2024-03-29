from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# from myFirstApp.account.models import UserActivity


def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        email = request.POST["email"]

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken!")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email is already registered!")
                return redirect("register")
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password1,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                )
                user.save()
                print("User created!")
                return redirect("login")
        else:
            messages.info(request, "Password is not matching!")
            return redirect("register")
        return redirect("/")
    else:
        return render(request, "register.html")


# Function for user login


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            # Create user login record
            # UserActivity.objects.create(user_id=user.id, last_login=datetime.now())
            return redirect("/")
        else:
            messages.info(request, "Invalid credentials!")
            return redirect("login")
    else:
        return render(request, "login.html")


# Function for user logout


def logout(request):
    auth.logout(request)
    return redirect("/")
