from django.views.generic.list import ListView
from .forms import ExpenseSearchForm
from .models import Expense, Category
# import functions summa, summary_per_date
from .reports import summary_per_category, summa, summary_per_date, count_per_category



class ExpenseListView(ListView):
    model = Expense
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list

        form = ExpenseSearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('name', '').strip()
            # adding field start date  in form for
            date_start = form.cleaned_data.get('date_start')
            # adding field finish date  in form
            date_finish = form.cleaned_data.get('date_finish')
            # adding field "category" in form
            category = form.cleaned_data.get('category')
            if name:
                print(name)
                queryset = queryset.filter(name__icontains=name)
                # block date search
            elif date_start:
                if date_finish:
                    # search from ... to...
                    queryset = queryset.filter(date__range=(date_start, date_finish))
                else:
                    # single date search
                    queryset = queryset.filter(date=date_start)
            # block category search
            elif category:
                queryset = queryset.filter(category__in=category)

        return super().get_context_data(
            form=form,
            object_list=queryset,
            summary_per_category=summary_per_category(queryset),
            # adding a function that calculates the sum spent
            total=summa(queryset),
            # adding a function sum by date
            summary_per_date=summary_per_date(queryset),
            **kwargs)



class CategoryListView(ListView):
    model = Category
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset= Expense.objects.all().values('category_id', "name")
        return super().get_context_data(
                count_per_category = count_per_category(queryset),
                **kwargs)

