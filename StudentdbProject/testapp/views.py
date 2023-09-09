from django.shortcuts import render
from testapp.models import StudentInfo3

# Create your views here.
def studentinfo_view(request):
    student_lists = StudentInfo3.objects.all()
    my_dict = {'student_lists': student_lists}
    return render(request, 'testapp/student.html', context=my_dict)
