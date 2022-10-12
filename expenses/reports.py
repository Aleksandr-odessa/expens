from collections import OrderedDict
from django.db.models import Sum, Value, Count
from django.db.models.functions import Coalesce
from django.db.models.functions import TruncMonth


def summary_per_category(queryset):
    return OrderedDict(sorted(
        queryset.annotate(category_name=Coalesce('category__name', Value('-')))
        .order_by()
        .values('category_name')
        .annotate(s=Sum('amount'))
        .values_list('category_name', 's')
    ))


# function calculates the sum spent
def summa(queryset):  #
    return queryset.aggregate(sum=Sum('amount')).get("sum")

# function calculates the total summary per year-month.
def summary_per_date(queryset):
    return OrderedDict(sorted(
        queryset
        .annotate(date_month=TruncMonth('date'))
        .order_by()
        .values('date_month')
        .annotate(s=Sum('amount'))
        .values_list('date_month', 's')
    ))

# function calculates number of expenses per category row in category list.
def count_per_category(queryset):
    b = queryset.annotate(category_name=Coalesce('category__name', Value('-'))).order_by()\
        .values('category_name')
    c = b.values_list('category_name', 'category_id')
    d = b.annotate(s=Count('amount'))
    e = d.values_list('category_name', 's')

    # print(f'b={b}')
    # print(f'c={c}')
    # print(f'd={d}')
    # print(f'e={e}')
    a = OrderedDict(sorted(e))
    return a

