# Generated by Django 3.2.15 on 2022-08-31 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='content',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
    ]