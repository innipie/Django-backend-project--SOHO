# Generated by Django 2.2.7 on 2019-12-01 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inaraApp', '0018_auto_20191201_0554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField(blank=True, max_length=520, null=True)),
                ('details', models.TextField(blank=True, max_length=520, null=True)),
                ('blog1', models.ImageField(blank=True, null=True, upload_to='home/')),
                ('blog2', models.ImageField(blank=True, null=True, upload_to='home/')),
                ('blog3', models.ImageField(blank=True, null=True, upload_to='home/')),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
