from django.shortcuts import render, redirect
from .models import Categoria, Foto
# Create your views here.


def Galeria(request):
    categoria = request.GET.get('categoria')
    if categoria == None:
        fotos = Foto.objects.all()
    else:
        fotos = Foto.objects.filter(categoria__nombre=categoria)

    categorias = Categoria.objects.all()

    data = {'categorias': categorias, 'fotos': fotos}
    return render(request, 'photos/galery.html', data)


def VerFoto(request, pk):
    foto = Foto.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'foto': foto})


def AgregarFoto(request):
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        formulario = request.POST
        imagen = request.FILES.get('imagen')
        if formulario['categoria'] != '':
            categoria = Categoria.objects.get(id=formulario['categoria'])
        elif formulario['categoria_nueva'] != '':
            categoria, creada = Categoria.objects.get_or_create(
                nombre=formulario['categoria_nueva'])
        else:
            categoria = None

        foto = Foto.objects.create(
            categoria=categoria,
            imagen=imagen,
            descripcion=formulario['descripcion'],
        )

        return redirect('galeria')

    return render(request, 'photos/add.html', {'categorias': categorias})
