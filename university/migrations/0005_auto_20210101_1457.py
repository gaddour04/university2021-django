# Generated by Django 3.0.3 on 2021-01-01 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0004_auto_20210101_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Universitie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('description', models.TextField()),
                ('image', models.TextField()),
                ('url', models.TextField(max_length=1000)),
                ('localisation', models.TextField(max_length=1000)),
                ('prix', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='university',
        ),
    ]
