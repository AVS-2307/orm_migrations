from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    # object_list = Student.objects.all()
    # Для каждого студента будет выполняться отдельный запрос.
    # Это не очень производительное решение - улучшите его с помощью prefetch_related
    object_list = Student.objects.prefetch_related('teachers')
    context = {'object_list': object_list}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)
