# Generated by Django 3.2.13 on 2022-05-21 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journey2app', '0002_alter_place_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='imgs')),
                ('details', models.TextField()),
            ],
        ),
    ]
