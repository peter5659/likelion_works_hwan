# Generated by Django 3.0.7 on 2020-07-26 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='writer',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
    ]