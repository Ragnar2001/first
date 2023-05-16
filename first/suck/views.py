from django.shortcuts import redirect, render
from suck.models import student
# Create your views here.

def models(request):
    if request.method =="POST":
      dt=request.POST
      name=dt.get('name')
      add=dt.get('add')
      subjects=dt.get('subjects')
      marks=dt.get('marks')
      student.objects.create(
          name=name,
          add=add,
          subjects=subjects,
          marks=marks,
      )
      return redirect('/models/')
    qr=student.objects.all()
    context={'data':qr}
    
    return render(request,'models.html',context)

def delete(request, id):
    de=student.objects.get(id=id)
    de.delete()
    return redirect('/models/')

def update(request,id):
    gr=student.objects.get(id=id)
    
    if request.method == "POST":
       dt=request.POST
       name=dt.get('name')
       add=dt.get('add')
       subjects=dt.get('subjects')
       marks=dt.get('marks') 
       gr.name=name
       gr.add=add
       gr.subjects=subjects
       gr.marks=marks
       gr.save()
       return redirect('/models/')
    context={'dota':gr}
    return render(request,'update.html',context)