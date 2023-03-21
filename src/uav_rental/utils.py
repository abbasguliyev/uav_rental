from django.utils.text import slugify

def generate_random_slug(name: str, query_list) -> str:
    slug = slugify(name)
    instances = query_list.filter(slug=slug)
    if instances.exists():
        slug_index = query_list.last().pk
        slug = slugify(f"{name}-{slug_index}")

    return slug