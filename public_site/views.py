from django.shortcuts import render, redirect
from engine_scanner.engine import Engine
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

def scanner(request, template_name="scanner2.html"):
    teste = "Olá, bem vindo ao SSRF Scan"
    return render(request, "scanner2.html", {'mensagem': teste})


def scanning(request):
    if request.method == "POST":
        engine = Engine(str(request.POST['domino_alvo']))
        urls = engine.get_urls()
        print(type(urls))
        return render(request, "scanner2.html", {'urls': urls})