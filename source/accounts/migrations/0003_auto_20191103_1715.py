# Generated by Django 2.2 on 2019-11-03 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191031_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='about',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='О себе '),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='user_pics', verbose_name='Аватар'),
        ),
    ]