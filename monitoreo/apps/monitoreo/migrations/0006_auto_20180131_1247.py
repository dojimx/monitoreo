# Generated by Django 2.0.1 on 2018-01-31 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoreo', '0005_auto_20180131_1245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monitoreo',
            old_name='medio',
            new_name='usuario',
        ),
        migrations.RemoveField(
            model_name='monitoreo',
            name='usuer',
        ),
    ]