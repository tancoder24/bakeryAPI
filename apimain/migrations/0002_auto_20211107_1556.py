# Generated by Django 3.1.7 on 2021-11-07 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apimain', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='all_ingridient',
            new_name='ingridient_quantities',
        ),
    ]