# Generated by Django 3.2.5 on 2021-09-02 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('business_field', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=150)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
