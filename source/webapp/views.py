from django.shortcuts import render, redirect

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
                return redirect('')
            else:
                return render(request, 'create.html', context={'form': form})