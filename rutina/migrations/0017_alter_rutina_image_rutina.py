# Generated by Django 4.1.2 on 2022-11-15 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rutina', '0016_delete_liststaff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rutina',
            name='image_rutina',
            field=models.ImageField(blank=True, null=True, upload_to='rutinas'),
        ),
    ]
