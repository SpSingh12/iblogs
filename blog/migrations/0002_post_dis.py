# Generated by Django 3.2.5 on 2021-09-02 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dis',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]