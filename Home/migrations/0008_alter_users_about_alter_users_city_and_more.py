# Generated by Django 4.2 on 2023-05-08 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_users_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='About',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='City',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='Country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='ProfilePhoto',
            field=models.ImageField(default='ProfilePhoto/default.png', null=True, upload_to='ProfilePhoto'),
        ),
        migrations.AlterField(
            model_name='users',
            name='Resume',
            field=models.FileField(default='Resume/default.pdf', null=True, upload_to='Resume'),
        ),
        migrations.AlterField(
            model_name='users',
            name='State',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='Street_address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='Zip',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
