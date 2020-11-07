# Generated by Django 3.0.7 on 2020-07-01 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0006_auto_20200701_2253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leasing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant', models.CharField(max_length=64)),
                ('company', models.CharField(blank=True, max_length=64, null=True)),
                ('phone', models.CharField(blank=True, max_length=16, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('suite', models.CharField(max_length=4)),
                ('since', models.DateField()),
                ('term_start', models.DateField()),
                ('term_end', models.DateField()),
                ('space', models.IntegerField()),
                ('unit', models.DecimalField(decimal_places=2, max_digits=7)),
                ('note', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Lease',
        ),
    ]
