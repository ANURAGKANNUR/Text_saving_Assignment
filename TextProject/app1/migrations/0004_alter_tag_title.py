# Generated by Django 3.2.15 on 2022-08-31 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_snippet_createdby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]