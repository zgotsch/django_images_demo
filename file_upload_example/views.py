import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ImageForm, Image


def index(request):
    images = Image.objects.all()[::-1]
    return render(request, "index.html", {"images": images})


def new(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.upload_time = datetime.datetime.now()
            image.save()
            return redirect("/")
    else:
        form = ImageForm()
    return render(request, "new_image.html", {"form": form})
