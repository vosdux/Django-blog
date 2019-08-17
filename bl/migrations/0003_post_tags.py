# Generated by Django 2.2.4 on 2019-08-16 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bl', '0002_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='bl.Tag'),
        ),
    ]