# Generated by Django 4.2 on 2023-05-12 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0014_remove_jobs_applecant_jobs_people_applyed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='People_applyed',
            field=models.ManyToManyField(blank=True, to='Home.applecant'),
        ),
    ]