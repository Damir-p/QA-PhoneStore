# Generated by Django 4.1.7 on 2023-02-27 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0003_rename_state_location_areas'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': 'Location', 'verbose_name_plural': 'Locations'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Product'},
        ),
    ]