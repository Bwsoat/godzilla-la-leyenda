# Generated by Django 4.1.7 on 2023-03-02 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_movie', models.CharField(max_length=100)),
                ('poster', models.ImageField(max_length=255, upload_to='posters/', verbose_name='Imagen')),
                ('description_text', models.CharField(max_length=300)),
                ('duration', models.CharField(max_length=50)),
                ('download', models.CharField(max_length=150)),
            ],
        ),
    ]
