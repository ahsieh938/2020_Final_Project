# Generated by Django 3.0.7 on 2020-06-30 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0015_auto_20200627_0358'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='serial',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]