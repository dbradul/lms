from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.template.defaulttags import register
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from student.forms import StudentAddForm, StudentEditForm, StudentDeleteForm
from student.models import Student


def index(request):
    return render(
        request=request,
        template_name='index.html',
    )


def students_list(request):

    qs = Student.objects.all().select_related('group')

    if request.GET.get('fname'):
        qs = qs.filter(first_name=request.GET.get('fname'))

    if request.GET.get('lname'):
        qs = qs.filter(last_name=request.GET.get('lname'))

    return render(
        request=request,
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

            student_exists = Student.objects.filter(
                Q(first_name=form.cleaned_data['first_name']) | \
                Q(email=form.cleaned_data['email'])
            ).exists()

            if not student_exists:
                student = form.save()
                print(f'Student created: {student}')
                return HttpResponseRedirect(reverse('students'))
            else:
                pass
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
            'title' : 'Student edit',
            'id' : student.id
        }
    )



def students_delete(request, id):

    try:
        student = Student.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Student with id={id} doesn't exist")

    if request.method == 'POST':
        form = StudentDeleteForm(
            data=request.POST,
            instance=student
        )

        if form.is_valid():
            result = student.delete()
            print(f'Student has been deleted: {result}')
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentDeleteForm(
            instance = student
        )

    return render(
        request=request,
        template_name='students_delete.html',
        context={
            'form' : form,
            'title' : f'Delete student {student}?'
        }
    )