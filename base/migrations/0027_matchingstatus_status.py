# Generated by Django 4.2.4 on 2023-08-31 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_matching_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchingstatus',
            name='status',
            field=models.IntegerField(null=True),
        ),
    ]