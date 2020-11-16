from django import forms
from datetime import datetime
from .models import Employee, JobPosition, Department


class EmployeeForm(forms.ModelForm):

    SALARY_TYPES = (
        ('m', 'monthly'),
        ('a', 'annually')
    )

    name = forms.CharField(
        label='* Name',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    department_id = forms.ModelChoiceField(
        label='* Department',
        queryset=Department.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    job_position_id = forms.ModelChoiceField(
        label='* Job Title',
        queryset=JobPosition.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    manager_id = forms.ModelChoiceField(
        label='Line Manager',
        queryset=Employee.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )
    salary = forms.FloatField(
        label='* Salary',
        required=True,
        max_value=10000,
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': "0.01"})
    )
    salary_type = forms.ChoiceField(
        label='* Salary Type', choices=SALARY_TYPES, widget=forms.Select(attrs={'class': 'form-control'}), 
        required=True
    )
    address = forms.CharField(
        label='* Address',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    created_at = forms.DateField(
        label='* Date Started',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        required=True,
        initial=datetime.now().date()
    )

    class Meta:
        model = Employee
        fields = [
            "name", "department_id", "job_position_id", "manager_id", "salary", "salary_type", "address", "created_at"
        ]
