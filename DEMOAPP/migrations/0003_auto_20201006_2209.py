# Generated by Django 3.0.6 on 2020-10-06 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DEMOAPP', '0002_hobby'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='auth',
        ),
        migrations.DeleteModel(
            name='Hobby',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]