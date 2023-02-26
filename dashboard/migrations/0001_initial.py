# Generated by Django 4.1.7 on 2023-02-25 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('markets', '0002_alter_location_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(max_length=100)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markets.location')),
            ],
            options={
                'verbose_name': 'Клиент(Customer)',
                'verbose_name_plural': 'Клиенты(Customers)',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(max_length=100)),
                ('tel_number', models.IntegerField()),
                ('position', models.CharField(max_length=100)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markets.location')),
            ],
            options={
                'verbose_name': 'Сотрудник / Сотрудница(Employee)',
                'verbose_name_plural': 'Сотрудники / Сотрудницы(Employees)',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.customer')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.employee')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markets.product')),
            ],
            options={
                'verbose_name': 'Заказы(Order)',
                'verbose_name_plural': 'Заказы(Orders)',
            },
        ),
    ]
