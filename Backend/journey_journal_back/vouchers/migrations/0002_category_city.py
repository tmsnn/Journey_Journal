# Generated by Django 4.2 on 2023-04-08 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vouchers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
