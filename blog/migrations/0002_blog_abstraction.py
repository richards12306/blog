# Generated by Django 3.0.3 on 2020-03-02 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='abstraction',
            field=models.TextField(default='nothing left', max_length=50),
        ),
    ]
