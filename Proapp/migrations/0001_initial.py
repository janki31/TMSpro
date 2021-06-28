# Generated by Django 3.1.2 on 2021-02-25 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image_gallery',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('image_name', models.CharField(max_length=50)),
                ('category', models.CharField(default='', max_length=100)),
                ('image_desc', models.TextField(default='')),
                ('image_file', models.ImageField(default='', upload_to='proapp/images')),
            ],
        ),
    ]