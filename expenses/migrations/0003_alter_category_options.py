# Generated by Django 4.1.2 on 2022-10-11 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_alter_category_options_category_count'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',)},
        ),
    ]