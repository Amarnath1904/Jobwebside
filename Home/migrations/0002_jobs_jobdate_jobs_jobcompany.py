# Generated by Django 4.2 on 2023-05-08 13:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='JObDate',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobs',
            name='JobCompany',
            field=models.CharField(default='apple', max_length=100),
            preserve_default=False,
        ),
    ]