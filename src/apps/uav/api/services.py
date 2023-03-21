from apps.uav.selectors import uav_list, category_list, brand_list
from apps.uav.models import Uav, Category, Brand
from uav_rental.utils import generate_random_slug

def create_uav(
    *, name: str,
    description: str = None,
    category = None,
    brand = None,
    weight: float,
    endurance: float,
    flight_range: float,
    max_speed: int,
    image,
    price: float
) -> Uav:
    slug=generate_random_slug(name, uav_list)
    obj = Uav.objects.create(
        name=name, slug=slug, description=description, category=category, brand=brand, weight=weight,
        endurance=endurance, flight_range=flight_range, max_speed=max_speed,
        image=image, price=price
    )
    return obj

def update_uav(instance, **data) -> Uav:
    obj = uav_list().filter(pk=instance.pk).update(**data)
    return obj

def create_category(category_name: str) -> Category:
    slug=generate_random_slug(category_name, uav_list)
    obj = Category.objects.create(category_name=category_name, slug=slug)
    return obj

def update_category(instance, **data) -> Category:
    obj = category_list().filter(pk=instance.pk).update(**data)
    return obj

def create_brand(brand_name: str) -> Brand:
    slug=generate_random_slug(brand_name, uav_list)
    obj = Brand.objects.create(brand_name=brand_name, slug=slug)
    return obj

def update_brand(instance, **data) -> Brand:
    obj = brand_list().filter(pk=instance.pk).update(**data)
    return obj
