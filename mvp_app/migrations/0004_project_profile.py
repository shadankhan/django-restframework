# Generated by Django 2.2.14 on 2021-02-05 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mvp_app', '0003_auto_20210204_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='profile',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='mvp_app.Profile'),
            preserve_default=False,
        ),
    ]
