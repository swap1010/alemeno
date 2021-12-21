from django.http import HttpResponse
from faker import Faker
import random
from .models import kid, image
import requests


def index(request):
    return HttpResponse("Hello, world. You're at the kids index.")


def add(request):
    fake = Faker()
    names = []
    for _ in range(5):
        name = fake.name()
        age = random.randint(2, 30)
        email = fake.email()
        num = random.randint(1000000000, 9999999999)
        k = kid(kid_name=name, parent_no=num, parent_email=email, kid_age=age)
        k.save()
    for KID in kid.objects.all():
        names.append(KID)
    for _ in range(50):
        res = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
        url = res.json()['meals'][0]["strMealThumb"]
        app = random.choice([True, False])
        by = fake.name()
        i = image(kid=random.choice(names), image_url=url, is_approved=app, Approved_by=by)
        i.save()
    return HttpResponse("5 kids and 50 images added")
