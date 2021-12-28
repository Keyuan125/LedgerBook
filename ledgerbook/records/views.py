from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Record
from records.forms import RecordForm

# Create your views here.

def RecordList(request):
    if request.method == 'GET':
        some_records = Record.objects.all()
        output = [r for r in some_records]
        record = RecordForm()
        context = {'records_list': output, 'form': record}
        return render(request, 'records/records.html', context)
    elif request.method == 'POST':
        form = RecordForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            form = form.save(commit=False)
            form.input_date = "2021-12-12"
            form.expense_income = 'expense'
            form.save()
            # redirect to a new URL:
        else:
            return HttpResponse('invalid')
    some_records = Record.objects.all()
    output = [r for r in some_records]
    record = RecordForm()
    context = {'records_list': output, 'form': record}
    return render(request, 'records/records.html', context)
        



