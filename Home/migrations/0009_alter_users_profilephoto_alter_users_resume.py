# Generated by Django 4.2 on 2023-05-08 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_alter_users_about_alter_users_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='ProfilePhoto',
            field=models.ImageField(null=True, upload_to='ProfilePhoto'),
        ),
        migrations.AlterField(
            model_name='users',
            name='Resume',
            field=models.FileField(null=True, upload_to='Resume'),
        ),
    ]