# Generated by Django 3.2 on 2021-06-29 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210629_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to='photos'),
        ),
    ]