# Generated by Django 4.0 on 2021-12-24 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(blank=True, max_length=100, null=True)),
                ('data', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(blank=True, max_length=220, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='images/')),
                ('is_liked', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]
