# Generated by Django 2.2.2 on 2019-07-11 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0003_auto_20190711_0914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work',
            old_name='unit',
            new_name='unit_price',
        ),
    ]