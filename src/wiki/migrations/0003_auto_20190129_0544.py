# Generated by Django 2.1.5 on 2019-01-29 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0002_urlpath_moved_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlpath',
            name='item_type',
            field=models.CharField(choices=[('article', 'Article'), ('category', 'Category')], default='category', max_length=20),
        ),
        migrations.AddField(
            model_name='urlpath',
            name='root_type',
            field=models.CharField(choices=[('wiki', 'Wiki'), ('npb', 'Regulations')], default='wiki', max_length=20),
        ),
    ]
