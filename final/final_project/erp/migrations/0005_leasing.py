# Generated by Django 3.0.7 on 2020-07-01 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('erp', '0004_delete_leasing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leasing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant', models.CharField(max_length=64)),
            ],
        ),
    ]
