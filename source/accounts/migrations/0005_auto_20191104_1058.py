# Generated by Django 2.2 on 2019-11-04 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20191103_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='github',
            field=models.URLField(blank=True, verbose_name='Ссылка на гитхаб'),
        ),
    ]
