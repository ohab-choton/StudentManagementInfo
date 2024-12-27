from django.shortcuts import render,get_object_or_404
from .models import Student
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import StudentForm


# Create your views here.

def index(request):
    return render(request, 'students/index.html' ,{'students': Student.objects.all()})

def view_student(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'students/view_student.html', {'student': student})

def add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            # Save the new student instance
            new_student = Student(
                student_number=form.cleaned_data['student_number'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                field_of_study=form.cleaned_data['field_of_study'],
                gpa=form.cleaned_data['gpa'],
            )
            new_student.save()

            # Show success message
            return render(request, 'students/add.html', {'form': StudentForm(), 'success': True})
        else:
            # If the form is invalid, return the form with errors
            return render(request, 'students/add.html', {'form': form})

    else:
        # If GET request, display a blank form
        form = StudentForm()

    return render(request, 'students/add.html', {'form': form})


def edit(request, id):
    student = get_object_or_404(Student, id=id)  # Safely retrieve the student object or return 404

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit.html', {'form': form, 'success': True, 'id': id})
        else:
            # If the form is invalid, re-render the form with errors and include the id
            return render(request, 'students/edit.html', {'form': form, 'id': id})
    else:
        # Handle GET request: render the form with the existing student data
        form = StudentForm(instance=student)
        return render(request, 'students/edit.html', {'form': form, 'id': id})

def delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return HttpResponseRedirect(reverse('index'))






