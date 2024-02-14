from django.shortcuts import render
from .models import Pessoa

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def salvar(request):
    nome = request.POST.get("nome")
    Pessoa.objects.create(nome=nome)
    email = request.POST.get("email")
    Pessoa.objects.create(email=email)
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})