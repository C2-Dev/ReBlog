# Generated by Django 2.1.5 on 2019-01-29 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190129_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
    ]
