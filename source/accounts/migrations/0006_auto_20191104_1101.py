# Generated by Django 2.2 on 2019-11-04 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20191104_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='github',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на гитхаб'),
        ),
    ]