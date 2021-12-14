from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LinkForm

from .models import Link


def home(request):
    link = Link.objects.all()

    data = {
        'links': link
    }

    return render(request, template_name='sentiment/sentiment.html', context=data)


def createpost(request):
    form = LinkForm()
    if request.method == 'POST':
        form = LinkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sentiment-url')

    data = {
        'form': form
    }
    return render(request, template_name='sentiment/search.html', context=data)


import csv


# Create your views here.
def getlink(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="links.csv"'
    links = Link.objects.all()
    writer = csv.writer(response)
    for link in links:
        writer.writerow([link])
    return response
