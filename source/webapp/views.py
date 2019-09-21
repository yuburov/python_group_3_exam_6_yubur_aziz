from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import BookForm
from webapp.models import G_book


def index_view(request):
    guests = G_book.objects.filter(status__startswith='active').order_by('created_at').reverse()
    return render(request, 'index.html', context={
        'guests': guests
    })

def book_create_view(request):
    if request.method == "GET":
        form = BookForm()
        return render(request, 'create.html', context={
            'form': form
        })
    elif request.method == 'POST':
            form = BookForm(data=request.POST)
            if form.is_valid():
                G_book.objects.create(name= form.cleaned_data['name'],
                email = form.cleaned_data['email'],
                text = form.cleaned_data['text'])
                return redirect('index')
            else:
                return render(request, 'create.html', context={'form': form})

def guest_update_view(request, pk):
    guest= get_object_or_404(G_book, pk=pk)
    if request.method == 'GET':
        form = BookForm(data={
            'name': guest.name,
            'email': guest.email,
            'text': guest.text,
        })
        return render(request, 'update.html', context={'form':form, 'guest': guest})
    elif request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            guest.name = form.cleaned_data['name']
            guest.email = form.cleaned_data['email']
            guest.text = form.cleaned_data['text']
            guest.save()
            return redirect('index')
        else:
            return render(request, 'update.html', context={'form': form, 'guest': guest})

def guest_delete_view(request, pk):
    guest = get_object_or_404(G_book, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'guest': guest})
    elif request.method == 'POST':
        guest.delete()
        return  redirect('index')

def search_guest(request):
    list=request.GET.getlist('search')
    guests= G_book.objects.filter(name__in=list)
    return render(request, 'index.html', context={
        'guests': guests
    })
