# Generated by Django 4.1 on 2022-08-26 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personality', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='is_feeler_extrovert',
            new_name='is_introvert',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='is_inhibited_introvert',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='is_social_introvert',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='is_thinker_extrovert',
        ),
    ]
