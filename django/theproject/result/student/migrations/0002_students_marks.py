# Generated by Django 2.2.2 on 2019-07-12 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='marks',
            field=models.CharField(default=90, max_length=100),
            preserve_default=False,
        ),
    ]
