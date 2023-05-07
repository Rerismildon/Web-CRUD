from django.shortcuts import redirect, render, get_object_or_404
from meuapp.models import Usuario
from meuapp.forms import UsuarioForm

def home(request):
    usuarios = Usuario.objects.all()       
    
    return render(request, 'Usuario/home.html', {
        "listaUsuarios" : usuarios,
    })
    
def insert(request):
    form = UsuarioForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('usuario.home')
    
    return render(request, 'Usuario/insert.html', {
        "form" : form,
    })
    
def edit(request, id, nome):
    usuarioSelect = get_object_or_404(Usuario, pk=id)
    form = UsuarioForm(request.POST or None, instance=usuarioSelect)
    
    
    if form.is_valid():
        form.save()
        return redirect('usuario.home')
    
    return render(request, 'Usuario/edit.html', {
        'form' : form,
        'nome' : nome
    })
    
def delete(request, id):
    usuarioSelect = get_object_or_404(Usuario, pk=id)
    usuarioSelect.delete()
    
    return redirect('usuario.home')
