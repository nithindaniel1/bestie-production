# Generated by Django 4.2.4 on 2023-09-05 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BestieAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resort_name', models.CharField(max_length=100)),
                ('resort_description', models.TextField()),
                ('resort_service', models.CharField(max_length=100)),
                ('resort_aminities', models.CharField(max_length=100)),
                ('resort_images', models.ImageField(upload_to='Resort_Image')),
                ('resort_slug', models.SlugField()),
                ('resort_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.packages')),
                ('resort_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Resort',
            },
        ),
    ]
