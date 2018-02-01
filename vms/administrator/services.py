from django.core.exceptions import ObjectDoesNotExist
from administrator.models import Administrator


def get_administrator_by_id(admin_id):

    is_valid = True
    result = None

    try:
        administrator = Administrator.objects.get(pk=admin_id)
    except ObjectDoesNotExist:
        is_valid = False

    if is_valid:
        result = administrator
    return result
