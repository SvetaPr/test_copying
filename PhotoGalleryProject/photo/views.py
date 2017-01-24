from django.shortcuts import render, render_to_response


# Create your views here.
from photo.models import Photography


def photos(request):
    return render_to_response('photos.html', {'photos': Photography.objects.all()})

def photo(request, photo_id=1):
    return render_to_response('photo.html', {'photo': Photography.objects.get(id=photo_id)})