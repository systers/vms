from django.http import HttpResponseRedirect


def test_redirect(request):
    return HttpResponseRedirect("/")
