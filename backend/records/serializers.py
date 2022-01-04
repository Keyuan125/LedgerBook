from rest_framework import serializers
from .models import Record

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['input_date', 'date', 'category', 'subCategory', 
                  'item', 'originalCurrency', 'newCurrency', 
                  'originalAmount', 'newAmount', 'comment', 'expense_income']

