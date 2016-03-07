from django import http
from django.conf import settings
from django.utils.translation import check_for_language
from django.utils.http import is_safe_url
def set_language(request):
    """
    Redirect to a given url while setting the chosen language in the
    session or cookie. The url and the language code need to be
    specified in the request parameters.

    Since this view changes how the user will see the rest of the site, it must
    only be accessed as a POST request. If called as a GET request, it will
    redirect to the page in the request (the 'next' parameter) without changing
    any state.

    NOTE: This function is almost the exact same as django's builtin
    set_language(), but this one always sets the language cookie when valid.
    django's function on the other hand, prioritises session over cookies
    """
    next = request.REQUEST.get('next')
    if not is_safe_url(url=next, host=request.get_host()):
        next = request.META.get('HTTP_REFERER')
        if not is_safe_url(url=next, host=request.get_host()):
            next = '/'
    response = http.HttpResponseRedirect(next)
    if request.method == 'POST':
        lang_code = request.POST.get('language', None)
        if lang_code and check_for_language(lang_code):
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
    return response
