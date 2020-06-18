import copy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Q

from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.core.exceptions import ObjectDoesNotExist

from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django_filters.views import FilterView

from student.filters import StudentListFilter
from student.forms import StudentAddForm, StudentEditForm
from student.models import Student



def students_add(request):

    if request.method == 'POST':
        form = StudentAddForm(request.POST)
        if form.is_valid():
            student = form.save()
            print(f'Student created: {student}')
            return HttpResponseRedirect(reverse('students:list'))
    else:
        form = StudentAddForm()

    return render(
        request=request,
        template_name='students_add.html',
        context={
            'form': form,
            'title': 'Student add'
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
            return HttpResponseRedirect(reverse('students:list'))
    else:
        form = StudentEditForm(
            instance=student
        )

    return render(
        request=request,
        template_name='students_edit.html',
        context={
            'form': form,
            'title': 'Student edit'
        }
    )


def students_delete(request, id):
    try:
        student = Student.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Student with id={id} doesn't exist")

    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students:list'))

    return render(
        request=request,
        template_name='students_delete.html',
        context={
            'student': student,
            'title': 'Student delete'
        }
    )


# class StudentsListView(LoginRequiredMixin, ListView):
#     model = Student
#     template_name = 'students_list.html'
#     context_object_name = 'students_list'
#     login_url = reverse_lazy('login')
#     paginate_by = 7
#
#     def get_queryset(self):
#         request = self.request
#         qs = super().get_queryset()
#         qs = qs.select_related('group')
#         qs = qs.order_by('-id')
#
#         if request.GET.get('search'):
#             qs = qs.filter(
#                 Q(first_name=request.GET.get('search'))
#             )
#         return qs

#
# from django_filters.views import FilterView

class StudentsListView(LoginRequiredMixin, FilterView):
    model = Student
    # filterset_class = StudentListFilter
    template_name = 'students_list.html'
    context_object_name = 'students_list'
    login_url = reverse_lazy('login')
    paginate_by = 7

    def get_queryset(self):
        request = self.request
        qs = super().get_queryset()
        qs = qs.select_related('group')
        qs = qs.order_by('-id')

        if request.GET.get('fname'):
            qs = qs.filter(
                Q(first_name=request.GET.get('fname'))
            )
        return qs

    # def get_context_data(self, *args, **kwargs):
    #     from urllib.parse import urlencode
    #     context = super().get_context_data(*args, **kwargs)
    #
    #     query_params = copy.deepcopy(self.request.GET)
    #     if 'page' in query_params:
    #         del query_params['page']
    #     context['query_params'] = urlencode(query_params)
    #
    #     return context

class StudentsUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    template_name = 'students_edit.html'
    form_class = StudentEditForm
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('students:list')


class StudentsCreateView(LoginRequiredMixin, CreateView):
    model = Student
    template_name = 'students_add.html'
    form_class = StudentAddForm
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Edit student'
        return context


class StudentsDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'students_delete.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('students:list')

