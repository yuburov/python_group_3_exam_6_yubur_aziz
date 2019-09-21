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
                BookForm.objects.create(name= form.cleaned_data['name'],
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
            return render(request, 'update.html', context={'form': form, 'guest': guest,})