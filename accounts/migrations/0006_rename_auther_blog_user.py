# Generated by Django 4.1.6 on 2023-05-06 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_blog_auther'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='auther',
            new_name='user',
        ),
    ]
