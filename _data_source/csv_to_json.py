import csv
import json
import os
from os import path

from django.db import models

# from ads.models import Ad, Category


def csv_to_json(csv_file: str, model):
    json_file = path.splitext(os.path.basename(csv_file))[0] + ".json"
    with open(csv_file, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        result = []
        for row in reader:
            if row.get('id'):
                del row['id']

            if row.get('price'):
                row['price'] = int(row['price'])

            if row.get('is_published'):
                row['is_published'] = bool(row['is_published'])

            result.append({'model': model, 'fields': row})
            # print(result)

        with open(json_file, "w", encoding="utf-8") as file:
            file.write(json.dumps(result, ensure_ascii=False))


def load_data_to_model(data, model):
    unit = model(**data)
    unit.save()


# unit = Ad
if __name__ == '__main__':
    csv_to_json(r"datasets/ads.csv", 'ads.ad')
    csv_to_json(r"datasets/categories.csv", 'ads.category')
