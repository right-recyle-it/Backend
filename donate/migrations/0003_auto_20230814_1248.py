# Generated by Django 3.2.20 on 2023-08-14 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0002_auto_20230814_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='donate',
            name='kind',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='donate',
            name='last_update',
            field=models.DateField(blank=True, null=True),
        ),
    ]
