# Generated by Django 3.1.3 on 2021-07-13 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shapes', '0003_auto_20210601_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='shapes',
            name='location',
            field=models.CharField(default=(0.25, 0.25), max_length=1000),
            preserve_default=False,
        ),
    ]
