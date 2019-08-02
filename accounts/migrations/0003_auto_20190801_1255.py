# Generated by Django 2.1.8 on 2019-08-01 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190731_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='role',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_line_manager',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_program_manager',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]