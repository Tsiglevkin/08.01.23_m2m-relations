# Generated by Django 4.1.5 on 2023-01-15 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_rename_tags_article_scopes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='scopes',
            new_name='tag',
        ),
    ]
