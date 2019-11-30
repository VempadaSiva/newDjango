from django.shortcuts import render,redirect
from .models import Note
from rest_framework import generics
from.Serializers import NoteSerializer

def all(request):
    return render(request, 'Details.html')

def save(request):
    uid=request.POST.get('id')
    title=request.POST.get('title')
    text=request.POST.get('text')
    date=request.POST.get('date')
    datee=request.POST.get('datee')
    if uid=='':
        s=Note(title=title,text=text,date=date,datee=datee)
        s.save()
        return render(request,'Details.html')
    else:
        s=Note.objects.filter(id=uid).update(title=title,text=text,date=date,datee=datee)
        return render(request, 'Details.html', {'s':s})
def data(request):
    data=Note.objects.all()
    return render(request, 'data.html', {'d':data})
def edit(request,id):
    edit=Note.objects.get(id=id)
    return render(request, 'Details.html', {'s':edit})
def delete(request,id):
    delete=Note.objects.get(id=id)
    delete.delete()
    return redirect(data)



class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'id'