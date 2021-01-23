from django.shortcuts import render, redirect

# Create your views here.

def home(request, template_name="index.html"):
    if request.method == "POST":
        nome=request.POST['name']
        sobrenome=request.POST['sobrenome']
        message=request.POST['message']
        redirect('home/')

    return render(request, template_name)