# Generated by Django 3.0.7 on 2020-07-01 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('erp', '0002_auto_20200625_0332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leasing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=16, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('suite', models.CharField(max_length=4)),
                ('since', models.DateField()),
                ('term_start', models.DateField()),
                ('term_end', models.DateField()),
                ('space', models.IntegerField()),
                ('unit', models.DecimalField(decimal_places=2, max_digits=7)),
                ('note', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
