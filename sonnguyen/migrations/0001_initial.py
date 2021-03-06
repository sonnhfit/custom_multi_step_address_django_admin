# Generated by Django 2.2 on 2020-03-10 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Resorts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='sonnguyen.Countries')),
            ],
        ),
        migrations.CreateModel(
            name='Tours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.ForeignKey(default=None, on_delete=None, to='sonnguyen.Countries')),
                ('resort', models.ForeignKey(default=None, null=True, on_delete=None, to='sonnguyen.Resorts')),
            ],
        ),
    ]
