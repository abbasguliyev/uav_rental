from django.contrib.auth import get_user_model
from apps.account.selectors import user_list

def create_user(
    *, email: str,
    first_name: str, last_name: str,
    is_staff: bool = False,
    is_active: bool = True,
    phone: str=None,
    address: str=None,
    company: str = None,
    groups: list = [],
    user_permissions: list = [],
    password: str
) -> get_user_model():
    obj = get_user_model().objects.create(
        email = email, first_name = first_name, last_name = last_name, is_staff = is_staff,
        is_active = is_active, phone=phone, address=address, company=company
    )
    obj.set_password(password)
    if user_permissions is not None:
        obj.user_permissions.set(user_permissions)
    if groups is not None:
        obj.groups.set(groups)
    obj.save()

    return obj

def update_user(instance, **data) -> get_user_model():
    obj = user_list().filter(pk=instance.pk).update(**data)
    return obj
