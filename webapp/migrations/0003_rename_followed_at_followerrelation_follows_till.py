# Generated by Django 4.0.4 on 2022-05-15 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_followerrelation_from_person_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='followerrelation',
            old_name='followed_at',
            new_name='follows_till',
        ),
    ]