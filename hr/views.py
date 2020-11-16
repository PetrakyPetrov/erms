# from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from .forms import EmployeeForm
from .models import Employee, Comment


@login_required(login_url='/auth/login/')
def index(request):

    searchWord = request.GET.get('search', None)
    searchWord = searchWord.strip() if searchWord else ""
    lowerSearchWord = searchWord.lower() if searchWord else ""

    page = request.GET.get('page', 1)
    employees_list = Employee.objects.all().order_by('-id')

    if searchWord:
        employees_list = employees_list.filter(
            Q(name__icontains=lowerSearchWord) |
            Q(department_id__name__icontains=lowerSearchWord) |
            Q(manager_id__name__icontains=lowerSearchWord) |
            Q(job_position_id__name__icontains=lowerSearchWord)
        )  # .exclude(deleted_at__isnull=False)

    page = request.GET.get('page', 1)
    paginator = Paginator(employees_list, 10)

    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        employees = paginator.page(1)
    except EmptyPage:
        employees = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'employees': employees, 'searchWord': searchWord})


@login_required(login_url='/auth/login/')
@permission_required('hr.add', raise_exception=True)
def createEmployee(request):

    req = request.POST
    form = EmployeeForm(req or None)
    relatedComments = []
    if form.is_valid():
        newEmployeeInstance = form.save()
        commentsList = req.getlist("comments[]", None)
        if commentsList:
            for comment in commentsList:
                comment = comment.strip()
                if len(comment) != 0:
                    cInstance = Comment(content=comment, author=request.user, employee_id=newEmployeeInstance)
                    cInstance.save()
        return redirect(index)

    return render(request, 'add-form.html', {
        'form': form,
        'relatedComments': relatedComments,
        'formName': 'Add Employee'
    })


@login_required(login_url='/auth/login/')
@permission_required('hr.edit', raise_exception=True)
def updateEmployee(request, id):

    employee = Employee.objects.get(id=id)
    req = request.POST
    relatedComments = Comment.objects.filter(employee_id=id)
    form = EmployeeForm(req or None, instance=employee)
    if form.is_valid():
        form.save()
        commentsList = req.getlist("comments[]", None)
        Comment.objects.filter(employee_id=id).delete()
        for comment in commentsList:
            comment = comment.strip()
            if len(comment) != 0:
                cInstance = Comment(content=comment, author=request.user, employee_id=employee)
                cInstance.save()
        return redirect(index)

    return render(request, 'add-form.html', {
        'form': form,
        'relatedComments': relatedComments,
        'formName': 'Edit Employee'
    })

@login_required(login_url='/auth/login/')
@permission_required('hr.delete', raise_exception=True)
def deleteEmployee(request, id):
    contact = Employee.objects.get(id=id)
    if request.method == 'GET':
        contact.delete()
    return redirect(index)
