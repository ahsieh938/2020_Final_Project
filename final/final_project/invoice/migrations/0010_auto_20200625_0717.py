# Generated by Django 3.0.7 on 2020-06-25 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0009_auto_20200625_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='po_num',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
