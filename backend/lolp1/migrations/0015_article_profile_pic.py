# Generated by Django 3.0.3 on 2021-03-19 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lolp1', '0014_remove_article_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
