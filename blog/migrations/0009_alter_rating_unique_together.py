# Generated by Django 4.2.11 on 2024-06-03 20:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_post_display_voting_alter_post_fighter1_name_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('post', 'user')},
        ),
    ]
