# Generated by Django 2.2.14 on 2021-02-04 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvp_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('image', models.ImageField(upload_to='static/project_image')),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
            ],
        ),
    ]