from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def login_view(request):
    return render(request, "users/login.html")

def register_view(request):

    if request.method == "POST":
        last_name = request.POST["last_name"]
        first_name =  request.POST["first_name"]
        email = request.POST["email"]
        username =  request.POST["username"]
        password =  request.POST["password"]
        print(last_name, first_name, email,username, password)
        print("La méthode POST")

        user = User.objects.create_user(
            username=username, 
            last_name=last_name,
            first_name=first_name,
            email=email,
            password=password,
            )
        return redirect('login')
    return render(request, "users/register.html")



