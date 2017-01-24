from django.shortcuts import render, render_to_response, redirect
from django.template.context_processors import csrf
from django.contrib import auth

from photo.forms import PhotoForm
from photo.models import Photography


def photos(request):
    args = {}
    args.update(csrf(request))
    args['form'] = PhotoForm
    args['photos'] = Photography.objects.all()
    args['username'] = auth.get_user(request).username
    return render_to_response('photos.html', args)

def photo(request, photo_id=1):
    return render_to_response('photo.html', {'photo': Photography.objects.get(id=photo_id),
                                             'username': auth.get_user(request).username})

def add_photo(request):
    if request.POST:
        form = PhotoForm(request.POST, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
    return redirect('/photos/')