# Generated by Django 2.1 on 2018-10-02 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20180911_0732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='previous_rating',
        ),
    ]
