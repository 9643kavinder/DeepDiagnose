
from .filters import CompanyFilter
from django.views import generic
from .models import CompanyDetail, Tests, Company, CompanyTests, OrderInfo
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from . forms import UserRegistrationForm, Company
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django import forms


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'deep_diagnose/register.html', {'form': form})


# for finding companies in a particular area
def home(request):
    return render(request, 'deep_diagnose/user_location.html')

# for finding companies in a particular area
def home(request):
    return render(request, 'deep_diagnose/user_location.html')


# for showing result --->companies nearby
def result(request):
    company_list = CompanyDetail.objects.all().order_by('company_name')
    company_filter = CompanyFilter(request.GET, queryset=company_list)
    return render(request, 'deep_diagnose/company_list.html', {'filter': company_filter})


# gives list of all the companies
class CompanyList(generic.ListView):
    template_name = 'deep_diagnose/all_companies.html'
    context_object_name = 'all_companies'

    def get_queryset(self):
        return CompanyDetail.objects.all().order_by('company_name')


# gives details about the company->tests,price,contact info
class CompanyDetails(generic.DetailView):
    model = CompanyDetail
    template_name = 'deep_diagnose/company_details.html'
    context_object_name = 'company'


# list of all tests
class TestList(generic.ListView):
    template_name = 'deep_diagnose/all_tests.html'
    context_object_name = 'all_tests'

    def get_queryset(self):
        return Tests.objects.all().order_by('test_name')


# gives details about selected test
class TestDetail(generic.DetailView):
    model = Tests
    template_name = 'deep_diagnose/test_detail.html'
    context_object_name = 'test'


# returns company name on the basis search item in searchbox
def put_list(request):
    polls = Tests.objects.all()
    search_term=''
    if 'search' in request.GET:
        search_term = request.GET['search']
        polls = polls.filter(test_name__istartswith=search_term)

    context = {'search_term': search_term, 'polls': polls, }
    return render(request, 'deep_diagnose/company_list.html', context)


def show_results(request, abc):
    # search=request.GET['search']
    polls = CompanyTests.objects.filter(tests__test_name=abc)
    """search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        polls = polls.filter(test__icontains=search_term)"""

    context = {
        'polls': polls
    }
    return render(request, 'deep_diagnose/base.html', context)


@login_required
def profile(request):
    return render(request, 'deep_diagnose/profile.html')


class OrderNow(CreateView):
    model = OrderInfo
    template_name = 'deep_diagnose/ordernow.html'
    fields = ['user_name', 'email_id','age','address_line_1','city','state','zip_code','phone_no',
              'suitable_date','suitable_time']
    success_url = reverse_lazy('deep_diagnose:find')


def thankyou(request):
    return render(request, 'deep_Diagnose/thankyou.html')


class TestCreate(CreateView):
    model = Tests
    fields = ['test_name', 'test_details']
    success_url = reverse_lazy('deep_diagnose:find')


class TestUpdate(UpdateView):
    model = Tests
    fields = ['test_name', 'test_details']
    success_url = reverse_lazy('deep_diagnose:find')


class TestDelete(DeleteView):
    model = Tests
    success_url = reverse_lazy('deep_diagnose:find')


class CompanyDelete(DeleteView):
    model = CompanyDetail
    success_url = reverse_lazy('deep_diagnose:find')


def create(request):

    if request.method == 'GET':

        form = Company()

        return render(request,'deep_diagnose/companyregister.html',{'form':form})

    if request.method == 'POST':
        form = Company(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password == confirm_password:
                form.save()
                form = Company()
                success = "Registered success"
                context = {
                    'not':success,
                    'form':form
                }
            else:
                form = Company()
                error = "password and confirm password doesnot not match"
                context = {
                    'not':error,
                    'form':form,
                }

        return render(request,'deep_diagnose/companyregister.html',context)


class AdminTestList(generic.ListView):
    template_name = 'deep_diagnose/admin_test_list.html'
    context_object_name = 'all_tests'

    def get_queryset(self):
        return Tests.objects.all().order_by('test_name')


class AdminCompanyList(generic.ListView):
    template_name = 'deep_diagnose/admin_company_list.html'
    context_object_name = 'all_companies'

    def get_queryset(self):
        return CompanyDetail.objects.all().order_by('company_name')

