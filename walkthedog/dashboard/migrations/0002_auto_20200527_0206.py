# Generated by Django 3.0.5 on 2020-05-26 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='coordinates',
            field=models.CharField(default='', max_length=150, verbose_name='координаты'),
        ),
    ]