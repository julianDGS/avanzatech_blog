# Generated by Django 5.0.3 on 2024-04-02 20:12

import django.db.models.deletion
from django.db import migrations, models

def create_default_team(apps, schema_editor):
    Team = apps.get_model("user", "Team")
    Team.objects.create(id=1, name='Rookie')

class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='name')),
            ],
            options={
                'db_table': 'teams',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='user.team'),
            preserve_default=False,
        ),
        migrations.RunPython(create_default_team),
    ]
