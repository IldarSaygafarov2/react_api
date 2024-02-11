from django.core.management import BaseCommand
import json
from api.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('products.json', mode='r', encoding='utf-8') as file:
            data = json.load(file)

            for item in data:
                obj = Product.objects.create(
                    title=item['title'],
                    description=item['description'],
                    price=item['price'],
                    rating=item['rating'],
                    image=item['image']
                )
                obj.save()
                print(f'Добавили {item["title"]}')