# Generated by Django 3.2.2 on 2021-05-07 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shapes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shapes',
            old_name='pic',
            new_name='pic1',
        ),
        migrations.AddField(
            model_name='shapes',
            name='pic2',
            field=models.ImageField(default='', upload_to='./photos'),
        ),
        migrations.AddField(
            model_name='shapes',
            name='pic3',
            field=models.ImageField(default='', upload_to='./photos'),
        ),
    ]
