# Generated by Django 4.1.7 on 2023-03-28 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_remove_tourismcompany_places_tourismplaces_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourismplaces',
            name='tourismCompany',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='api.tourismcompany'),
        ),
    ]
