# Generated by Django 3.1.7 on 2021-03-27 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shit',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]
