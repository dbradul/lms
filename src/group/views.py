
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from group.forms import GroupEditForm, GroupAddForm
from group.models import Group


# Create your views here.
def groups_list(request):
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