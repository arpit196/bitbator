# Generated by Django 3.1.7 on 2021-06-06 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collab', '0009_auto_20210605_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='allowRequest',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
