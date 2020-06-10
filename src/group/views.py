
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import UpdateView, CreateView, DeleteView, ListView

from group.forms import GroupEditForm, GroupAddForm
from group.models import Group

#
# # Create your views here.
# def groups_list(request):
#     qs = Group.objects.all()#.select_related('students')
#
#     if request.GET.get('name'):
#         qs = qs.filter(name__startswith=request.GET.get('name'))
#
#     if request.GET.get('course'):
#         qs = qs.filter(course__contains=request.GET.get('course'))
#
#     return render(
#         request=request,
#         template_name='group_list.html',
#         context={
#             'group_list' : qs,
#             'title': 'Group list'
#         }
#     )
#
# def group_edit(request, id):
#     try:
#         group = Group.objects.get(id=id)
#     except ObjectDoesNotExist:
#         return HttpResponseNotFound(f"Group with id={id} doesn't exist")
#
#     if request.method == 'POST':
#         form = GroupEditForm(request.POST, instance=group)
#
#         if form.is_valid():
#             group = form.save()
#             print(f'Group has been saved: {group}')
#             return HttpResponseRedirect(reverse('groups'))
#     else:
#         form = GroupEditForm(
#             instance = group
#         )
#
#     return render(
#         request=request,
#         template_name='group_edit.html',
#         context={
#             'form' : form,
#             'title' : 'Group edit',
#             'group' : group
#         }
#     )
#


def groups_list(request):
    qs = Group.objects.all()

    if request.GET.get('name'):
        qs = qs.filter(name__startswith=request.GET.get('name'))

    if request.GET.get('course'):
        qs = qs.filter(course__contains=request.GET.get('course'))

    return render(
        request=request,
        template_name='group_list.html',
        context={
            'group_list': qs,
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
            instance=group
        )

    return render(
        request=request,
        template_name='group_edit.html',
        context={
            'form': form,
            'title': 'Group edit',
            'group': group
        }
    )



class GroupsListView(ListView):
    model = Group
    template_name = 'group_list.html'
    context_object_name = 'group_list'

    def get_queryset(self):
        request = self.request
        qs = super().get_queryset()
        # qs = qs.select_related('group')
        # qs = qs.order_by('-id')

        # if request.GET.get('fname'):
        #     qs = qs.filter(first_name=request.GET.get('fname'))
        #
        # if request.GET.get('lname'):
        #     qs = qs.filter(last_name=request.GET.get('lname'))

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Group list'
        return context


class GroupsUpdateView(UpdateView):
    model = Group
    template_name = 'group_edit.html'
    form_class = GroupEditForm

    def get_success_url(self):
        return reverse('groups:list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        # context['title'] = 'Group list'
        return context

class GroupsCreateView(CreateView):
    model = Group
    template_name = 'group_add.html'
    form_class = GroupAddForm

    def get_success_url(self):
        return reverse('groups:list')


class GroupsDeleteView(DeleteView):
    model = Group
    template_name = 'group_delete.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('groups:list')

