from django.shortcuts import render
from first_app.models import AccessRecord


def index(request):
    access_records = AccessRecord.objects.select_related('name', 'user').order_by('date')
    my_dict = {"access_records": access_records}
    return render(request, 'first_app/index.html', context=my_dict)
