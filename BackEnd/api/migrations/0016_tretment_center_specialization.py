# Generated by Django 4.1.7 on 2023-03-27 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_remove_websiteusers_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='tretment_center',
            name='specialization',
            field=models.CharField(choices=[('Dental', 'Dental'), ('Hair Implant', 'Hair Implant')], default='Dental', max_length=20),
        ),
    ]
