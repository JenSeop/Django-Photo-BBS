from django.shortcuts import render
from .models import Phto

# Create your views here.
# def phto_list(request):
#     return render(request, 'photo/photo_list.html', {})
def photo_list(request):
    photos = Phto.objects.all()
    return render(request, 'photo/photo_list.html', {'photos': photos})