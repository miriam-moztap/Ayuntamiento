# Generated by Django 4.2.10 on 2024-03-03 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_usuario_options_remove_usuario_birthdate_and_more'),
        ('expedientes', '0004_expediente_abogado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente',
            name='abogado',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='users.usuario', verbose_name='Usuario_id'),
        ),
    ]
