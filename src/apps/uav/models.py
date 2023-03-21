from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(_("category_name"), max_length=155)
    slug = models.SlugField(max_length=255, unique=True)

    def get_absolute_url(self):
        return reverse("category-detail", kwargs={"slug": self.slug})
    
    def __str__(self) -> str:
        return self.category_name

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

class Brand(models.Model):
    brand_name = models.CharField(_("category_name"), max_length=155)
    slug = models.SlugField(max_length=255, unique=True)
    
    def get_absolute_url(self):
        return reverse("brand-detail", kwargs={"slug": self.slug})
    
    def __str__(self) -> str:
        return self.brand_name

    class Meta:
        verbose_name = "brand"
        verbose_name_plural = "brands"


class Uav(models.Model):
    name = models.CharField(_("name"), max_length=200)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey("uav.Category", on_delete=models.SET_NULL, null=True, blank=True, related_name="uavs")
    brand = models.ForeignKey("uav.Brand", on_delete=models.SET_NULL, null=True, blank=True, related_name="uavs")
    weight = models.FloatField(_("weight"), default=0)
    endurance = models.FloatField(_("endurance"), default=0)
    flight_range = models.FloatField(_("flight range"), default=0)  
    max_speed = models.PositiveIntegerField(_("max_speed"), default=0)
    image = models.ImageField(upload_to="uav", default="default.jpg", blank=True, null=True)
    price = models.DecimalField(default=0, max_digits=20, decimal_places=2)

    def get_absolute_url(self):
        return reverse("uav-detail", kwargs={"slug": self.slug})
    
    class Meta:
        ordering = ("pk",)
        verbose_name = "uav"
        verbose_name_plural = "uavs"
    
    def __str__(self) -> str:
        return self.name

