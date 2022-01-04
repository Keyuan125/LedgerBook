from django.forms import ModelForm
from records.models import Record

class RecordForm(ModelForm):
    class Meta:
        model = Record
        exclude = ('input_date', 'expense_income')
        