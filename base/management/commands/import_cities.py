import json
import os

from django.core.management.base import BaseCommand
from django.db import transaction


class Command(BaseCommand):
    def handle(self, *args, **options):
        from django.conf import settings
        from base.models import City
        file = os.path.join(settings.STATIC_DIR, 'static_json_files/estados_municipios.json')
        if os.path.isfile(file):
            cities = []
            with open(file, "r") as data:
                for obj in json.load(data):
                    if obj['model'] == 'localidades.cidade':
                        _field = obj['fields']
                        try:
                            city = City(uf=_field.get('codigo'),
                                        name=str(_field.get('nome')),
                                        geoIBGEId=_field.get('codigo_ibge'))
                            cities.append(city)
                        except Exception as e:
                            print(str(e))
                if cities:
                    with transaction.atomic():
                        _records = City.objects.bulk_create(cities)
                        print(f'{len(_records)}, municipios incluidos')

