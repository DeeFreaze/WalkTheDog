from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion



class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100, verbose_name='Location')),
                ('date', models.DateField(verbose_name='Дата выполнения заказа')),
                ('start_of_walk', models.CharField(max_length=10, verbose_name='start_of_walk ')),
                ('end_of_walk', models.CharField(max_length=10, verbose_name='end_of_walk')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('breed', models.CharField(max_length=100, verbose_name='Breed')),
                ('size', models.IntegerField(verbose_name='Size')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Price')),
                ('status', models.CharField(choices=[('Completed', 'Completed'), ('Accepted', 'Accepted'), ('Running', 'Running'), ('Canceled', 'Canceled')], default='Accepted', max_length=100, null=True, verbose_name='Статус заказа')),
                ('additional_option', models.CharField(blank=True, default='', max_length=200, verbose_name='Дополнительные опции')),
                ('coordinates', models.CharField(blank=True, default='', max_length=150, verbose_name='координаты')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
