from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0003_orders_orderupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.URLField(default='https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400&q=80', max_length=500),
        ),
    ]
