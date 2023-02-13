from django.shortcuts import render
from mycourse.models import *

def home(request):
    data1 = Dept.objects.all()
    for dept in data1:
        print(dept.dept_id, dept.name)

    data2 = Course.objects.all()
    for course in data2:
        print(course.course_id, course.name)

    data3 = Student.objects.all()
    for student in data3:
        print(student.user, student.dept_id, student.prn, student.name, student.DOB)

    return render(request, 'index.html', {'query1': data1,'query2': data2,'query3': data3})
