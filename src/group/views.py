from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from group.forms import GroupEditForm, GroupAddForm
from group.models import Group
from student.forms import StudentAddForm, StudentEditForm, StudentDeleteForm
from student.models import Student


# Create your views here.
def group_list(request):
    qs = Group.objects.all()#.select_related('students')

    if request.GET.get('name'):
        qs = qs.filter(name__startswith=request.GET.get('name'))

    if request.GET.get('course'):
        qs = qs.filter(course__contains=request.GET.get('course'))

    return render(
        request=request,
        template_name='group_list.html',
        context={
            'group_list' : qs,
            'title': 'Group list'
        }
    )


def group_add(request):

    if request.method == 'POST':
        form = GroupAddForm(request.POST)
        if form.is_valid():

            group_exists = Group.objects.filter(
                Q(name=form.cleaned_data['name'])
            ).exists()

            if not group_exists:
                group = form.save()
                print(f'Group has been created: {group}')
                return HttpResponseRedirect(reverse('groups'))
            else:
                pass
    else:
        form = GroupAddForm()

    return render(
        request=request,
        template_name='group_add.html',
        context={
            'form' : form,
            'title' : 'Group add'
        }
    )



def group_edit(request, id):
    try:
        group = Group.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Group with id={id} doesn't exist")

    if request.method == 'POST':
        form = GroupEditForm(request.POST, instance=group)

        if form.is_valid():
            group = form.save()
            print(f'Group has been saved: {group}')
            return HttpResponseRedirect(reverse('groups'))
    else:
        form = GroupEditForm(
            instance = group
        )

    return render(
        request=request,
        template_name='group_edit.html',
        context={
            'form' : form,
            'title' : 'Group edit',
            'group' : group
        }
    )



def group_delete(request, id):

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