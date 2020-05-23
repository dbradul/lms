from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from student.forms import StudentAddForm, StudentEditForm
from student.models import Student


def students_list(request):
    qs = Student.objects.all().select_related('group')

    if request.GET.get('fname'):
        qs = qs.filter(first_name=request.GET.get('fname'))

    if request.GET.get('lname'):
        qs = qs.filter(last_name=request.GET.get('lname'))

    result = '<br>'.join(
        str(student)
        for student in qs
    )

    # return HttpResponse(result)
    return render(        request=request,
        template_name='students_list.html',
        context={
            'students_list' : qs,
            'title': 'Student list'
        }
    )


def students_add(request):

    if request.method == 'POST':
        form = StudentAddForm(request.POST)
        if form.is_valid():
            student = form.save()
            print(f'Student created: {student}')
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentAddForm()

    return render(
        request=request,
        template_name='students_add.html',
        context={
            'form' : form,
            'title' : 'Student add'
        }
    )


def students_edit(request, id):

    try:
        student = Student.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Student with id={id} doesn't exist")

    if request.method == 'POST':
        form = StudentEditForm(request.POST, instance=student)

        if form.is_valid():
            student = form.save()
            print(f'Student created: {student}')
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentEditForm(
            instance = student
        )

    return render(
        request=request,
        template_name='students_edit.html',
        context={
            'form' : form,
            'title' : 'Student edit'
        }
    )
