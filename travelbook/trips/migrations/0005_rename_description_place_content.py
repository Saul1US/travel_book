# Generated by Django 4.0.5 on 2022-06-17 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0004_placeentry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='description',
            new_name='content',
        ),
    ]
