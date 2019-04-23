# Generated by Django 2.2 on 2019-04-23 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('activated', models.BooleanField(default=False)),
                ('slug', models.SlugField(null=True)),
            ],
        ),
    ]
