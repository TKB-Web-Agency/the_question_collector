# Generated by Django 3.2.4 on 2021-07-25 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210724_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]
