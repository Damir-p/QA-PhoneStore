# Generated by Django 4.1.7 on 2023-02-28 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_customer_options_alter_employee_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={},
        ),
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]