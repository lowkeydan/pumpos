# Generated by Django 2.2.2 on 2019-07-11 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='department',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]