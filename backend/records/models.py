from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Record(models.Model):
    input_date = models.DateTimeField()
    date = models.DateTimeField()
    category = models.CharField(max_length=20, default='')
    subCategory = models.CharField(max_length=20, default='')
    item = models.TextField(default='')
    originalCurrency = models.CharField(max_length=5, default='')
    newCurrency = models.CharField(max_length=5, null=True)
    originalAmount = models.FloatField(null=True)
    newAmount = models.FloatField(null=True)
    comment = models.TextField(default='')
    # Indicate if it's an expense or income
    expense_income = models.CharField(max_length=10)
    
    def __str__(self):
        return self.item