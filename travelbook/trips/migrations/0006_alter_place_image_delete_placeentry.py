# Generated by Django 4.0.5 on 2022-06-18 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0005_rename_description_place_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='PlaceEntry',
        ),
    ]