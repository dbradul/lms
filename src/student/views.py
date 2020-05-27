from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from student.forms import StudentAddForm, StudentEditForm
from student.models import Student


class StudentBaseView(LoginRequiredMixin):
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse('students:list')


class StudentsListView(StudentBaseView, ListView):
    model = Student
    template_name = 'students_list.html'
    context_object_name = 'students_list'
    paginate_by = 10

    def get_queryset(self):
        request = self.request
        qs = super().get_queryset()
        qs = qs.select_related('group')
        qs = qs.order_by('-id')

        if request.GET.get('search'):
            qs = qs.filter(
                Q(first_name=request.GET.get('search'))
            )
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Student list'
        return context


class StudentsUpdateView(StudentBaseView, UpdateView):
    model = Student
    template_name = 'students_edit.html'
    form_class = StudentEditForm


class StudentsCreateView(StudentBaseView, CreateView):
    model = Student
    template_name = 'students_add.html'
    form_class = StudentAddForm


class StudentsDeleteView(StudentBaseView, DeleteView):
    model = Student
    template_name = 'students_delete.html'
    pk_url_kwarg = 'id'

