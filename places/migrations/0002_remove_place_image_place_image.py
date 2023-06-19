# Generated by Django 4.2.2 on 2023-06-19 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='image',
        ),
        migrations.AddField(
            model_name='place',
            name='image',
            field=models.ManyToManyField(blank=True, null=True, to='places.placeimages'),
        ),
    ]
