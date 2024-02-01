from django.shortcuts import render, redirect
from .models import Human
from django.core import serializers
import os

# Create your views here.
def Index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        image = request.FILES.get('image')
        address = request.POST.get('address')
        if image:
            humanNew = Human.objects.create(name = name, email= email, age=int(age), gender= gender, image=image, address=address)
            humanNew.save()
        else:
            humanNew = Human.objects.create(name = name, email= email, age=int(age), gender= gender, address=address)
            humanNew.save()

        # print(name, email,age,gender, image, address)
    return render(request, 'my_app/index.html')


def Profiles(request01):
    human = Human.objects.all()

    return render(request01, 'my_app/all_prof.html',locals())


def delete_prof(request, id):
    prof = Human.objects.get(id=id)
    if prof.image != 'def.jpg':
        os.remove(prof.image.path)

    prof.delete()

    return redirect('Profiles')


def update(request, id):
    prof = Human.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        image = request.FILES.get('image')
        address = request.POST.get('address')

        if image:
            prof.name = name
            prof.email= email
            prof.age=int(age)
            prof.gender= gender
            if prof.image != 'def.jpg':
                os.remove(prof.image.path)
            prof.image=image
            prof.address=address
            prof.save()
            return redirect('Profiles')
        else:
            prof.name = name
            prof.email= email
            prof.age=int(age)
            prof.gender= gender
            prof.address=address
            prof.save()
            return redirect('Profiles')
        

        # print(name, email,age,gender, image, address)
    return render(request, 'my_app/update.html', locals())