# Generated by Django 2.0.1 on 2018-01-31 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoreo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitoreo',
            name='medio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medio.Medio'),
        ),
    ]
