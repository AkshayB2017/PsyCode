# Generated by Django 3.0.2 on 2020-02-19 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='language',
            field=models.CharField(default='null', max_length=10),
            preserve_default=False,
        ),
    ]
