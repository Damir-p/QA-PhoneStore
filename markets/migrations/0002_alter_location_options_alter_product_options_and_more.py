# Generated by Django 4.1.7 on 2023-02-25 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': 'Локация(Location)', 'verbose_name_plural': 'Локация(Locations)'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар(Product)', 'verbose_name_plural': 'Товары(Product)'},
        ),
        migrations.RemoveField(
            model_name='location',
            name='age',
        ),
        migrations.RemoveField(
            model_name='location',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='location',
            name='location',
        ),
        migrations.AddField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='desctiption',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
