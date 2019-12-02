# Generated by Django 2.2.7 on 2019-11-27 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(blank=True, max_length=6)),
                ('second', models.CharField(blank=True, max_length=18)),
                ('third', models.TextField(blank=True, max_length=520, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='home/')),
            ],
        ),
    ]
