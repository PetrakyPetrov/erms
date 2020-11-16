from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import django


class Comment(models.Model):

    content = models.CharField(max_length=50)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    employee_id = models.ForeignKey("Employee", default=None, on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=True, blank=True, default=datetime.now())

    def __str__(self):
        return self.content


class Department(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class JobPosition(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Employee(models.Model):

    SALARY_TYPES = (
        ('m', 'monthly'),
        ('a', 'annually')
    )

    name = models.CharField(max_length=50, blank=False, default="")
    department_id = models.ForeignKey('Department', on_delete=models.DO_NOTHING, blank=False, default=None)
    job_position_id = models.ForeignKey('JobPosition', on_delete=models.DO_NOTHING, blank=False, default=None)
    manager_id = models.ForeignKey('Employee', on_delete=models.DO_NOTHING, null=True, blank=True, default=None)
    salary = models.FloatField()
    salary_type = models.CharField(max_length=1, choices=SALARY_TYPES)
    address = models.CharField(max_length=255, blank=False, default="")
    comment_id = models.ForeignKey('Comment', on_delete=models.DO_NOTHING, null=True, blank=True, default=None)
    created_at = models.DateField(null=True, blank=True, default=django.utils.timezone.now)

    class Meta:
        permissions = (
            ('add', 'Add'),
            ('edit', 'Edit'),
            ('delete', 'Delete'),
        )

    def __str__(self):
        return self.name

    def get_salary_type(self):
        return dict(self.SALARY_TYPES)[self.salary_type]
