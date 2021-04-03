# Generated by Django 3.0.4 on 2020-03-29 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('price', models.FloatField()),
                ('author', models.CharField(max_length=30)),
                ('publisher', models.CharField(max_length=50)),
            ],
        ),
    ]
