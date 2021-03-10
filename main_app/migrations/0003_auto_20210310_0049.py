# Generated by Django 3.1.7 on 2021-03-10 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_fav_list_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fav_list',
            name='fav_players',
        ),
        migrations.RemoveField(
            model_name='fav_player',
            name='user',
        ),
        migrations.AddField(
            model_name='fav_player',
            name='fav_list',
            field=models.ForeignKey(default=16, on_delete=django.db.models.deletion.CASCADE, to='main_app.fav_list'),
            preserve_default=False,
        ),
    ]
