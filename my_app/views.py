from django.shortcuts import render
from .models import Image
from .forms import ImageUploadForm

def home(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    imgs = Image.objects.all()
    form = ImageUploadForm()
    return render(request, 'my_app/home.html', {"form":form, "imgs": imgs})
