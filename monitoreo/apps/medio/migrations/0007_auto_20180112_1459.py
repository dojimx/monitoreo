# Generated by Django 2.0.1 on 2018-01-12 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medio', '0006_auto_20180105_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=50)),
                ('tn', models.CharField(choices=[('EST', 'ESTATAL'), ('NAC', 'NACIONAL'), ('INT', 'INTERNACIONAL')], max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='palabra',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Palabra',
        ),
    ]