# Generated by Django 3.0.4 on 2020-03-27 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateField(null=True),
        ),
    ]
