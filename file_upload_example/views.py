import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ImageForm, Image


def index(request):
    images = Image.objects.all()[::-1]
    return render(request, "index.html", {"images": images})


def new(request):
    if request.method == "POST":
        # print(repr(request.POST))
        # print(repr(request.FILES))
        upload_time = datetime.datetime.now()
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.upload_time = upload_time
            image.save()

            manual_image = Image()
            manual_image.image = request.FILES["manual_image"]
            manual_image.upload_time = upload_time
            manual_image.save()

            return redirect("/")
    else:
        form = ImageForm()
    return render(request, "new_image.html", {"form": form})
