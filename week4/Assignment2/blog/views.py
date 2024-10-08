from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Student
from .forms import StudentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q  # For complex queries
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.

def student_list(request):
    query = request.GET.get('q')  # Get the search query
    if query:
        students = Student.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
    else:
        students = Student.objects.all()  # Show all students if no search query

    # Pagination logic
    paginator = Paginator(students, 5)  # Display 10 students per page
    page_number = request.GET.get('page')  # Get the current page number from the request
    page_obj = paginator.get_page(page_number)  # Get the appropriate page

    context = {
        "students": page_obj,  # Pass the page object to the template
        "paginator": paginator,  # Optional: pass paginator if you need it for extra logic
        "query": query,  # Pass the query to retain it in the search bar
    }
    return render(request, "blog/student_list.html", context)


def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)  # Automatically raises 404 if student does not exist
    return render(request, "blog/student_detail.html", {"student": student})


@login_required
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    
    return render(request, 'blog/add_student.html', {'form': form})

@login_required
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

