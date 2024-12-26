from django.shortcuts import render,get_object_or_404
from .models import Student
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def index(request):
    return render(request, 'students/index.html' ,{'students': Student.objects.all()})

def view_student(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'students/view_student.html', {'student': student})

