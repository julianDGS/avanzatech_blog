# Generated by Django 5.0.3 on 2024-04-04 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permission', '0003_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('public', 'Public'), ('auth', 'Authenticate'), ('team', 'Team'), ('author', 'Author')], default=None, max_length=20, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='name',
            field=models.CharField(choices=[('read', 'Read'), ('edit', 'Edit')], default=None, max_length=10, unique=True, verbose_name='name'),
        ),
    ]
