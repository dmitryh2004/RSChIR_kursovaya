# Generated by Django 5.1.1 on 2024-11-16 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0010_queuelist_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='queuelist',
            name='timeout',
            field=models.IntegerField(default=30),
        ),
    ]
