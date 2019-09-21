from django.shortcuts import render
from webapp.models import G_book


def index_view(request):
    guests = G_book.objects.filter(status__startswith='active').order_by('created_at').reverse()
    return render(request, 'index.html', context={
        'guests': guests
    })

