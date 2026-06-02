#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
echo "from django.contrib.auth import get_user_model; U = get_user_model(); U.objects.filter(username='admin').exists() or U.objects.create_superuser('admin', 'admin@example.com', 'Admin@1234')" | python manage.py shell
python manage.py shell -c "from ecommerceapp.models import Product; Product.objects.all().delete(); print('Old products cleared')"
python manage.py loaddata products.json
echo "Products loaded successfully"
