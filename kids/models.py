from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone


class kid(models.Model):
    kid_name = models.CharField(max_length=100, primary_key=True, null=False)
    kid_age = models.PositiveSmallIntegerField(null=False)
    phone_regex = RegexValidator(regex=r'^\d{10,10}$',
                                 message="Enter without code(10 digits)")
    parent_no = models.CharField(validators=[phone_regex], max_length=10, blank=False)
    parent_email = models.EmailField(max_length=254, null=False)

    def __str__(self):
        return self.kid_name


class image(models.Model):
    kid = models.ForeignKey(kid, on_delete=models.CASCADE)
    image_url = models.URLField(null=False)
    created_on = models.DateTimeField(default=timezone.now, editable=False)
    updated_on = models.DateTimeField(default=timezone.now)
    is_approved = models.BooleanField()
    Approved_by = models.CharField(max_length=100)
    FOOD_CHOICES = (
        ("1", "Vegetarian"),
        ("2", "Fruit"),
        ("3", "Grain"),
        ("4", "protein"),
        ("5", "Dessert"),
        ("6", "Unknown"),
    )
    Group = models.CharField(max_length=20, choices=FOOD_CHOICES, default="6")

    def __str__(self):
        return self.kid.kid_name

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe(f'<img src="{self.image_url}" height=200px width=200px/>')

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
