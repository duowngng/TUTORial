# Generated by Django 4.2.4 on 2023-08-30 04:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_remove_point_point_remove_question_subtopic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.topic'),
        ),
        migrations.AlterField(
            model_name='review',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
