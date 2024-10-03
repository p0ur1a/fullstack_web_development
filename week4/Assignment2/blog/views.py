from django.shortcuts import render, get_object_or_404
from blog.models import Student

# Create your views here.

def student_list(request):
    students = Student.objects.all()
    context = {"students": students}
    return render(request, "blog/student_list.html", context)

# def student_detail(request, student_id):
#     student = get_object_or_404(Student, id=student_id)
#     context = {"student": student}
#     return render(request, "blog/student_detail.html", context)