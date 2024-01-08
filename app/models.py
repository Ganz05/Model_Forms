from django.db import models

# Create your models here.
class School(models.Model):
    sname=models.CharField(max_length=100,primary_key=True)
    sloc=models.CharField(max_length=100)
    sprincipal=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.sname

class Branch(models.Model):
    sname=models.ForeignKey(School,on_delete=models.CASCADE)
    bname=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.bname

class Student(models.Model):
    sname=models.ForeignKey(School,on_delete=models.CASCADE)
    bname=models.ForeignKey(Branch,on_delete=models.CASCADE)
    student_name=models.CharField(max_length=100,default=None)
    DOB=models.DateField()

    def __str__(self) -> str:
        return self.student_name
