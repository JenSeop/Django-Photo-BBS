from django.shortcuts import render, get_object_or_404
from .models import Phto

# Create your views here.
# def phto_list(request):
#     return render(request, 'photo/photo_list.html', {})
def photo_list(request):
    photos = Phto.objects.all()
    return render(request, 'photo/photo_list.html', {'photos': photos})

def photo_detail(request, pk):
    photo = get_object_or_404(Phto, pk=pk)
    return render(request, 'photo/photo_detail.html', {'photo': photo})