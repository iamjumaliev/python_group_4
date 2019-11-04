# Generated by Django 2.2 on 2019-11-03 18:20

from django.db import migrations

def create_profiles(apps, schema_editor):

    User = apps.get_model('auth', 'User')

    UserProfile = apps.get_model('accounts', 'UserProfile')

    for user in User.objects.all():

        UserProfile.objects.get_or_create(user=user)

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20191103_1715'),
    ]

    operations = [
        migrations.RunPython(create_profiles),
    ]