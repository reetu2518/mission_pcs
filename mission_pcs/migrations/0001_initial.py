# Generated by Django 3.0.8 on 2020-07-28 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('mob', models.IntegerField()),
            ],
        ),
    ]
