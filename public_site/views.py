from django.shortcuts import render, redirect

# Create your views here.

def home(request, template_name="index.html"):
    if request.method == "POST":
        nome = request.POST['name']
        usernameGitHub = request.POST['github']
        email = request.POST['email']
        uf = request.POST['uf']
        message = request.POST['message']
        redirect('home/')

    return render(request, template_name)

def scanner(request, template_name="scanner.html"):
    return render(request, template_name)

