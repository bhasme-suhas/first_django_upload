# Generated by Django 4.2.4 on 2023-08-10 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Products",
            fields=[
                ("product_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("product_name", models.CharField(max_length=255)),
            ],
        ),
    ]
