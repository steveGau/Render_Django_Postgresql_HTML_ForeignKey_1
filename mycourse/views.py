from django.shortcuts import render
# from mycourse.models import *
from .models import Dept, Course, Student

def home(request):
    data1 = Dept.objects.all()
    data2 = Course.objects.all()
    data3 = Student.objects.all()
    for dept in data1:
        print(dept.dept_id, dept.name)

    for course in data2:
        print(course.course_id, course.name)
        

    for student in data3:
        print(student.user, student.dept_id, student.prn, student.name, student.DOB)

    return render(request, 'index.html', {'query1': data1,'query2': data2,'query3': data3})

'''
ProgrammingError at /
relation "mycourse_dept" does not exist
LINE 1: ...urse_dept"."dept_id", "mycourse_dept"."name" FROM "mycourse_...
                                                             ^
Request Method:	GET
Request URL:	https://render-django-postgresql-html-foreignkey-qka2.onrender.com/
Django Version:	4.1.6
Exception Type:	ProgrammingError
Exception Value:	
relation "mycourse_dept" does not exist
LINE 1: ...urse_dept"."dept_id", "mycourse_dept"."name" FROM "mycourse_...
                                                             ^
Exception Location:	/opt/render/project/src/.venv/lib/python3.10/site-packages/django/db/backends/utils.py, line 89, in _execute
Raised during:	mycourse.views.home
'''