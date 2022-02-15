from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render

from student.models import Students, Rating

def home(request):
    student = Students.objects.all()
    student_fst = Students.objects.get(id=1) # select * from Student where id=1
    student_flt = Students.objects.filter(name="Aikumush")
    return render(request, 'index.html' , {"student": student})

def student_list(request):
    labels = []
    data = []

    queryset = Rating.objects.values('students__fio').annotate(student_ball=Sum('ball')).order_by(
        '-id')
    for entry in queryset:
        labels.append(entry['students__fio'])
        data.append(entry['student_ball'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
