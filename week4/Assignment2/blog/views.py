from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Student
from .forms import StudentForm

# Create your views here.

def student_list(request):
    students = Student.objects.all()
    context = {"students": students}
    return render(request, "blog/student_list.html", context)

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    context = {"student": student}
    return render(request, "blog/student_detail.html", context)


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    
    return render(request, 'blog/add_student.html', {'form': form})

# def edit_student(request, student_id):
#     student = get_object_or_404(Student, id=student_id)
    
#     if request.method == "POST":
#         form = StudentForm(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#             return redirect('student_list')
#     else:
#         form = StudentForm(instance=student)
    
#     return render(request, 'blog/edit_student.html', {'form': form, 'student': student})

def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == "POST":
        if 'save' in request.POST:
            form = StudentForm(request.POST, instance=student)
            if form.is_valid():
                form.save()
                return redirect('student_list')
        elif 'delete' in request.POST:
            student.delete()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'blog/edit_student.html', {'form': form, 'student': student})