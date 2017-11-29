from django import forms
from expense.models import Expense


class ExpenseForms(forms.ModelForm):

    

	class Meta:
		model = Expense
		fields = ('item','amount','date')
        