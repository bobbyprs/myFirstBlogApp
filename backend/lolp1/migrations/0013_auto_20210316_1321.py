# Generated by Django 3.1.1 on 2021-03-16 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lolp1', '0012_article_photofilename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='PhotoFileName',
        ),
        migrations.AddField(
            model_name='article',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
