# Generated by Django 4.2 on 2023-05-08 16:41

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0013_alter_user_email'),
        ('Home', '0002_jobs_jobdate_jobs_jobcompany'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('ProfilePhoto', models.ImageField(default='ProfilePhoto/default.png', upload_to='ProfilePhoto')),
                ('Resume', models.FileField(default='Resume/default.pdf', upload_to='Resume')),
                ('Street_address', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=100)),
                ('Zip', models.CharField(max_length=100)),
                ('About', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
