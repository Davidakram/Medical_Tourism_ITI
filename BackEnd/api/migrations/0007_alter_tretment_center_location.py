# Generated by Django 4.1.7 on 2023-03-26 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_medicalreservation_status_tourismreservation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tretment_center',
            name='location',
            field=models.DecimalField(decimal_places=5, max_digits=50),
        ),
    ]
