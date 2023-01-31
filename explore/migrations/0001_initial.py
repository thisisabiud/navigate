# Generated by Django 4.1 on 2023-01-31 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
    ]
