from django.shortcuts import render
from app.views import *
from app.forms import *
from django.http import HttpResponse

# Create your views here.

def insert_school(request):
    ELFO=SchoolForm()
    d={'ELFO':ELFO}
    if request.method=='POST':
        CLSO=SchoolForm(request.POST)
        if CLSO.is_valid():
            CLSO.save()
            return HttpResponse('Data Inserted Succussfully')
         
    return render(request,'insert_school.html',d)

def insert_branch(request):
    ELBO=BranchForm()
    d={'ELBO':ELBO}
    if request.method=='POST':
        CLBO=BranchForm(request.POST)
        if CLBO.is_valid():
            CLBO.save()
            return HttpResponse('Data Inserted Succussfully' )
        
    return render(request,'insert_branch.html',d)

def insert_student(request):
    ELSTO=StudentForm()
    d={"ELSTO":ELSTO}
    if request.method=='POST':
        CLSTO=StudentForm(request.POST)
        if CLSTO.is_valid():
            CLSTO.save()
            return HttpResponse('Data Inserted Succcussfully')

    return render(request,'insert_student.html',d)

