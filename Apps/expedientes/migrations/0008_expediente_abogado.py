# Generated by Django 4.2.10 on 2024-03-03 22:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expedientes', '0007_remove_expediente_abogado'),
    ]

    operations = [
        migrations.AddField(
            model_name='expediente',
            name='abogado',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario_id'),
        ),
    ]
