from .models import CompanyDetail, CompanyTests
import django_filters


class CompanyFilter(django_filters.FilterSet):
    class Meta:
        model = CompanyDetail
        fields = ['city', 'state', ]


