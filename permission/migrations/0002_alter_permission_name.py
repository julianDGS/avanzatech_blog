# Generated by Django 5.0.3 on 2024-04-04 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permission', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='name',
            field=models.CharField(choices=[('read', 'Read'), ('edit', 'Edit')], default=None, max_length=10, verbose_name='name'),
        ),
    ]
