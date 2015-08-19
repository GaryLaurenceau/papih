from rest_framework.exceptions import NotAuthenticated


def get_key(key, user):
    try:
        return key.objects.get(owner=user)
    except Exception, e:
        raise NotAuthenticated()
