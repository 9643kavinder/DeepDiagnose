from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'deep_diagnose'

urlpatterns = [
    # url('/', views.redirecting, name='redirecting'),
    url(r'^register/', views.register, name='register'),
    # /home/
    # for finding nearby companies
    url(r'^home/$', views.home, name='find'),


    # /
    # /company/id(1,2..)
    # giving company details like tests and their price
    url(r'^company/(?P<pk>[0-9]+)/$', views.CompanyDetails.as_view(), name='company_detail'),

    # /test_list/
    # for list of all tests
    url(r'^test_list/$', views.TestList.as_view(), name='test_list'),

    # /result/
    # shows result according to users location
    url(r'^result/$', views.result, name='result'),

    # /test/pk(1,2 ..)
    # for test details like about_test companies offering that test with price
    url(r'^tests/(?P<pk>[0-9]+)/$', views.TestDetail.as_view(), name='tests_detail'),

    url(r'^response/$', views.put_list, name='response'),

    path('response1/<str:abc>', views.show_results),

    path('profile/', views.profile, name='profile'),

    path('ordernow/(?P<pk>[0-9]+)', views.OrderNow, name='ordernow'),

    path('thankyou/', views.thankyou, name='thankyou'),

    url(r'test/add/$', views.TestCreate.as_view(), name='test-add'),

    url(r'test/update/(?P<pk>[0-9]+)/$', views.TestUpdate.as_view(), name='test-update'),

    url(r'test/(?P<pk>[0-9]+)/delete/$', views.TestDelete.as_view(), name='test-delete'),

    url(r'company/(?P<pk>[0-9]+)/delete/$', views.CompanyDelete.as_view(), name='company-delete'),


    url(r'^admin_test_list/$', views.AdminTestList.as_view(), name='admin_test_list'),

    url(r'^admin_company_list/$', views.AdminCompanyList.as_view(), name='admin_company_list'),

    path('adminhome/', views.adminhome, name='adminhome'),

    url(r'^login-admin/$', views.loginAdminPanel, name='admin-login'),

    path('adminprofile/', views.adminprofile, name='admin-profile'),

    path('company/', views.CompanyList.as_view(), name='companylist'),

    url(r'category(?P<pk>[0-9]+)/$', views.Category.as_view(), name='category'),

    path('orderhistory/', views.OrderHistory, name='orderhistory'),
    url(r'order/(?P<pk>[0-9]+)/cancel/$', views.CancelOrder.as_view(), name='cancel-order'),
    url(r'order/(?P<pk>[0-9]+)/update/$', views.OrderUpdate.as_view(), name='update-order'),

    url(r'^search',views.search_titles),#renders ajax_search.html
]
