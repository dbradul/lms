from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from webargs import fields
from webargs.djangoparser import use_kwargs, use_args

from students.models import Student
from students.utils import format_records
from django.core.exceptions import BadRequest
from webargs import djangoparser


def hello(request):
    return HttpResponse('SUCCESS')


parser = djangoparser.DjangoParser()


@parser.error_handler
def handle_error(error, req, schema, *, error_status_code, error_headers):
    raise BadRequest(error.messages)


@parser.use_args(
    {
        "first_name": fields.Str(
            required=False,
        ),
        "text": fields.Str(
            required=False,
            validate=[lambda x: False]
        ),
    },
    location="query",
)
def get_students(request, params):

    students = Student.objects.all()

    for param_name, param_value in params.items():
        students = students.filter(**{param_name: param_value})

    result = format_records(students)

    return HttpResponse(result)
