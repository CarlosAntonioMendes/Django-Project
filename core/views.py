from django.shortcuts import render, redirect, get_object_or_404
from .models import Pessoa

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def salvar(request):
    if request.method == 'POST':
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        

        if nome and email:
            try:

                pessoa = Pessoa.objects.create(nome=nome, email=email)
            except Exception as e:

                error_message = f"Error creating Pessoa object: {str(e)}"
                return render(request, "error.html", {"error_message": error_message})
            
            pessoas = Pessoa.objects.all()
            return render(request, "index.html", {"pessoas": pessoas})
        else:

            error_message = "Nome and email are required."
            return render(request, "error.html", {"error_message": error_message})
    else:

        error_message = "Only POST requests are allowed."
        return render(request, "error.html", {"error_message": error_message})

def editar(request,id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, "editar.html", {"pessoa": pessoa})

def update(request, id):
        
        vnome = request.POST.get("nome")
        vemail = request.POST.get("email")
        

        pessoa = get_object_or_404(Pessoa, id=id)
        

        pessoa.nome = vnome
        pessoa.email = vemail
        pessoa.save()
        

        return redirect(home) 

def delete(request, id):

    pessoa = get_object_or_404(Pessoa, id=id)
    
    pessoa.delete()
    
 
    return redirect(home)  