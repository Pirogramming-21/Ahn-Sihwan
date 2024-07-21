# Generated by Django 5.0.7 on 2024-07-21 12:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pirostagram', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='post_images/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='pirostagram.post')),
            ],
        ),
    ]
