# Generated by Django 4.2 on 2023-05-08 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0011_jobs_peopleapplied'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='peopleApplied',
        ),
        migrations.AddField(
            model_name='jobs',
            name='Apply',
            field=models.ManyToManyField(blank=True, related_name='Apply', to='Home.users'),
        ),
    ]
