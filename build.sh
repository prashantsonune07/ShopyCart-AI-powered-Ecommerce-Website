#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py shell -c "from ecommerceapp.models import Product; Product.objects.all().delete(); print('Old products cleared')"
python manage.py loaddata products.json
echo "Products loaded successfully"
