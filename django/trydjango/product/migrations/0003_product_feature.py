# Generated by Django 2.2.2 on 2019-07-07 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20190707_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='feature',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
