# Generated by Django 4.2.2 on 2023-08-31 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0027_matchingstatus_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(1, 'Student'), (2, 'Teacher')], default='1'),
        ),
    ]
