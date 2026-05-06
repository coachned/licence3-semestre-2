from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login


def login_view(request):
    
    if request.method== "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, "users/login.html", context={"error":"Nom d'utilisateur ou mot de passe incorect"})
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

        if User.objects.filter(email=email).count() > 0:
            return render(request, "users/register.html", context={"error":"Adresse mail déjà attribuée"})
        
        if User.objects.filter(username=username).count() > 0:
            return render(request, "users/register.html", context={"error":"Nom d'utilisateur déjà existant"})


        user = User.objects.create_user(
            username=username, 
            last_name=last_name,
            first_name=first_name,
            email=email,
            password=password,
            )
        return redirect('login')
    return render(request, "users/register.html")



