from django import forms
from .models import Expense, Category


class ExpenseSearchForm(forms.ModelForm, forms.Form):
    class Meta:
        model = Expense
        fields = ('name',)

    # adding title choice for category
    title_choice =Category.objects.all().values_list()

    # adding field strart date for search on form
    date_start = forms.DateField(required=False, label='Date from')
    # adding field finish date for search on form
    date_finish = forms.DateField(required=False, label='Date to')
    # adding field category for searching by multiple categories.
    category = forms.MultipleChoiceField(required=False, choices=title_choice)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False


