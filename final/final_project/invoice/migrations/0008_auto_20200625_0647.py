# Generated by Django 3.0.7 on 2020-06-25 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0007_auto_20200625_0631'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='address',
            new_name='address1',
        ),
        migrations.AddField(
            model_name='customer',
            name='address2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
