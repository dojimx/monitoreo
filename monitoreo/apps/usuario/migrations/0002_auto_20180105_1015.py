# Generated by Django 2.0.1 on 2018-01-05 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='asignado',
            field=models.ManyToManyField(to='usuario.Asignacion'),
        ),
    ]
