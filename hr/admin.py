from django.contrib import admin
from django import forms
from .models import JobPosition, Employee, Department, Comment


class CommentInline(admin.TabularInline):
    model = Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ["content", "author", "employee_id", "created_at"]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


class EmployeeAdminForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            "name", "department_id", "job_position_id", "manager_id", "salary", "salary_type", "address", "created_at"
        ]


class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        "name", "department_id", "job_position_id", "manager_id", "salary", "salary_type", "address", "created_at"
    ]
    form = EmployeeAdminForm
    inlines = [
        CommentInline,
    ]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.author = request.user
            instance.save()
        formset.save_m2m()


class JobPositionAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]


admin.site.register(JobPosition, JobPositionAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Employee, EmployeeAdmin)
