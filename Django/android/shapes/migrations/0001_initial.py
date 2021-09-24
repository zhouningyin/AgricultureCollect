# Generated by Django 3.1.3 on 2021-02-08 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shapes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('croptype', models.CharField(max_length=4)),
                ('shapesdescrip', models.CharField(max_length=1000)),
                ('pic', models.ImageField(upload_to='./photos')),
            ],
        ),
    ]
