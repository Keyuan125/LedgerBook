from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Record
from records.forms import RecordForm

from rest_framework import viewsets, generics
from .serializers import RecordSerializer
from .models import Record


# Create your views here.

# def RecordList(request):
#     if request.method == 'GET':
#         some_records = Record.objects.all()
#         output = [r for r in some_records]
#         record = RecordForm()
#         context = {'records_list': output, 'form': record}
#         return render(request, 'records/records.html', context)
#     elif request.method == 'POST':
#         form = RecordForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             form = form.save(commit=False)
#             form.input_date = "2021-12-12"
#             form.expense_income = 'expense'
#             form.save()
#             # redirect to a new URL:
#         else:
#             return HttpResponse('invalid')
#     some_records = Record.objects.all()
#     output = [r for r in some_records]
#     record = RecordForm()
#     context = {'records_list': output, 'form': record}
#     return render(request, 'records/records.html', context)
        

class RecordList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class RecordView(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

class RecordDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = Record.objects.all()
    serializer_class = RecordSerializer