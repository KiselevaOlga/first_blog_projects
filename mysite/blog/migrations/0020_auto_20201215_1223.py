# Generated by Django 3.1.2 on 2020-12-15 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_postcommentator'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcommentator',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='postcommentator',
            name='posts',
            field=models.ManyToManyField(related_name='commentators', to='blog.Post'),
        ),
    ]
