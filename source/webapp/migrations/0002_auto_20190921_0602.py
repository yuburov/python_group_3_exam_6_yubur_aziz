# Generated by Django 2.2 on 2019-09-21 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g_book',
            name='status',
            field=models.CharField(choices=[('active', 'Активно'), ('blocked', 'Заблокировано')], max_length=20, verbose_name='Статус'),
        ),
    ]