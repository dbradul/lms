from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from student.forms import StudentAddForm, StudentEditForm
from student.models import Student

#
# def students_list(request):
#     qs = Student.objects.all().select_related('group')
#
#     if request.GET.get('fname'):
#         qs = qs.filter(first_name=request.GET.get('fname'))
#
#     if request.GET.get('lname'):
#         qs = qs.filter(last_name=request.GET.get('lname'))
#
#     return render(        request=request,
#         template_name='students_list.html',
#         context={
#             'students_list' : qs,
#             'title': 'Student list'
#         }
#     )
#
#
# def students_add(request):
#
#     if request.method == 'POST':
#         form = StudentAddForm(request.POST)
#         if form.is_valid():
#             student = form.save()
#             print(f'Student created: {student}')
#             return HttpResponseRedirect(reverse('list'))
#     else:
#         form = StudentAddForm()
#
#     return render(
#         request=request,
#         template_name='students_add.html',
#         context={
#             'form' : form,
#             'title' : 'Student add'
#         }
#     )
#
#
# def students_edit(request, id):
#
#     try:
#         student = Student.objects.get(id=id)
#     except ObjectDoesNotExist:
#         return HttpResponseNotFound(f"Student with id={id} doesn't exist")
#
#     if request.method == 'POST':
#         form = StudentEditForm(request.POST, instance=student)
#
#         if form.is_valid():
#             student = form.save()
#             print(f'Student created: {student}')
#             return HttpResponseRedirect(reverse('list'))
#     else:
#         form = StudentEditForm(
#             instance = student
#         )
#
#     return render(
#         request=request,
#         template_name='students_edit.html',
#         context={
#             'form' : form,
#             'title' : 'Student edit'
#         }
#     )
#
#
# def students_delete(request, id):
#     try:
#         student = Student.objects.get(id=id)
#     except ObjectDoesNotExist:
#         return HttpResponseNotFound(f"Student with id={id} doesn't exist")
#
#     if request.method == 'POST':
#         student.delete()
#         return HttpResponseRedirect(reverse('list'))
#
#     return render(
#         request=request,
#         template_name='students_delete.html',
#         context={
#             'student' : student,
#             'title' : 'Student delete'
#         }
#     )


class StudentListView(ListView):
    model = Student
    template_name = 'students_list.html'
    context_object_name = 'students_list'

    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.GET.get('fname'):
            qs = qs.filter(first_name=self.request.GET.get('fname'))

        if self.request.GET.get('lname'):
            qs = qs.filter(last_name=self.request.GET.get('lname'))

        qs = qs.select_related('group')
        qs = qs.order_by('-id')
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context.update({'title':'Students list'})
        return context


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students_edit.html'
    # fields = '__all__'
    # success_url = reverse_lazy('student:list')
    form_class = StudentEditForm

    def post(self, request, *args, **kwargs):
        print('...')
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('student:list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context.update({'title':'Student update'})
        return context


class StudentCreateView(CreateView):
    model = Student
    template_name = 'students_add.html'
    fields = '__all__'
    success_url = reverse_lazy('student:list')


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students_delete.html'
    success_url = reverse_lazy('student:list')
    context_object_name = 'student42'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context.update({'title':'Student delete'})
        return context

# class StudentViewSet(GenericViewSet)