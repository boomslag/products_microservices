# Generated by Django 3.2.16 on 2023-04-06 23:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0010_auto_20230404_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user', models.UUIDField(blank=True)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('comment', models.TextField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
