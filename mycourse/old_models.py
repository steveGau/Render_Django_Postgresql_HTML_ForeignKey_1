from django.db import models
from django.contrib.auth.models import User
# Create your models here.

'''
class Dept(models.Model):
    # dept_id = models.CharField(primary_key='True', max_length=100)
    dept_id = models.IntegerField(primary_key='True')
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
'''

class Dept(models.Model):
    dept_id = models.CharField(primary_key='True', max_length=100)
    # dept_id = models.IntegerField(primary_key='True')
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Course(models.Model):
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    course_id = models.CharField(primary_key='True', max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    dept_id = models.ForeignKey(Dept, on_delete=models.CASCADE, default=1)
    prn = models.CharField(primary_key='True', max_length=100)
    name = models.CharField(max_length=200)
    DOB = models.DateField(default='1998-01-01')

    def __str__(self):
        return self.name
        
# how to create ForeignKey in a table of postgres database inside postgres and not using python        

'''
convert the following python django postgres table code to psql commands

class Dept(models.Model):
    dept_id = models.CharField(primary_key='True', max_length=100)
    name = models.CharField(max_length=200)

CREATE TABLE dept (
    dept_id varchar(100) PRIMARY KEY,
    name varchar(200)
);


class Dept(models.Model):
    dept_id = models.IntegerField(primary_key='True')
    name = models.CharField(max_length=200)

CREATE TABLE dept (
    dept_id INTEGER PRIMARY KEY,
    name VARCHAR(200)
);

'''

'''
convert the following python django postgres table code to psql commands

class Course(models.Model):
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    course_id = models.CharField(primary_key='True', max_length=50)
    name = models.CharField(max_length=50)
    
CREATE TABLE course (
    dept_id varchar(100),
    course_id varchar(50) PRIMARY KEY,
    name varchar(50),
    FOREIGN KEY (dept_id) REFERENCES dept(dept_id) ON DELETE CASCADE
);

CREATE TABLE course (
    course_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(50),
    dept_id INTEGER REFERENCES dept(dept_id) ON DELETE CASCADE
);

'''

'''
convert the following python django postgres table code to psql commands

class Student(models.Model):
    prn = models.CharField(primary_key='True', max_length=100)
    dept_id = models.ForeignKey(Dept, on_delete=models.CASCADE, default=1)



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    dept_id = models.ForeignKey(Dept, on_delete=models.CASCADE, default=1)
    prn = models.CharField(primary_key='True', max_length=100)
    name = models.CharField(max_length=200)
    DOB = models.DateField(default='1998-01-01')

user_id integer REFERENCES auth_user(id) ON DELETE CASCADE,
    dept_id integer REFERENCES dept(id) ON DELETE CASCADE,
        FOREIGN KEY (user_id) REFERENCES auth_user(id) ON DELETE CASCADE

dept =    models.ForeignKey(Dept, on_delete=models.CASCADE)
dept_id = models.ForeignKey(Dept, on_delete=models.CASCADE, default=1)

dept_id varchar(100),
FOREIGN KEY (dept_id) REFERENCES dept(dept_id) ON DELETE CASCADE
FOREIGN KEY (dept_id) REFERENCES dept(dept_id) ON DELETE CASCADE,

    FOREIGN KEY (user_id) REFERENCES auth_user(id) ON DELETE CASCADE,
    
    
CREATE SCHEMA IF NOT EXISTS schema_name;

CREATE TABLE schema_name.student (
    prn varchar(100) PRIMARY KEY,
    dept_id integer REFERENCES dept(id) ON DELETE CASCADE DEFAULT 1
);

    
CREATE TABLE student (
    id serial PRIMARY KEY,
    FOREIGN KEY (dept_id) REFERENCES dept(dept_id) ON DELETE CASCADE,
    prn character varying(100) UNIQUE,
    name character varying(200),
    dob date
);


CREATE TABLE student (
    prn VARCHAR(100) PRIMARY KEY,
    name VARCHAR(200),
    dept_id INTEGER REFERENCES dept(dept_id) ON DELETE CASCADE DEFAULT 1,
    dob DATE DEFAULT '1998-01-01',
    user_id INTEGER REFERENCES auth_user(id) ON DELETE CASCADE
);    
    
'''


'''


'''