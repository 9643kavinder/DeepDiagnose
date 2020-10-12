from .models import Tests, CompanyDetail, TestCategory, CompanyTests

def basetest1(request):

    hello = Tests.objects.all()

    return {
        'testname': hello,

    }


def basetest2(request):

    labs = CompanyDetail.objects.all()
    return {
        'labsname': labs
    }


def basetest3(request):

    category = TestCategory.objects.all()
    return {
        'cat': category
    }


def cost(request):
    ct=CompanyTests.objects.all().order_by('-cost')
    return{'ct':ct}