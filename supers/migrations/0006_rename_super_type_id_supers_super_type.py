# Generated by Django 4.1 on 2022-08-30 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supers', '0005_rename_super_type_supers_super_type_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supers',
            old_name='super_type_id',
            new_name='super_type',
        ),
    ]