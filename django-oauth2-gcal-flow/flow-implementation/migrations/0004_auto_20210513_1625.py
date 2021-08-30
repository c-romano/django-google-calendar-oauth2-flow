# Generated by Django 3.1.6 on 2021-05-13 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeblocker', '0003_googleuser_credentials'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='googleuser',
            name='credentials',
        ),
        migrations.AddField(
            model_name='googleuser',
            name='client_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='googleuser',
            name='client_secret',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='googleuser',
            name='default_scopes',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='googleuser',
            name='id_token',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='googleuser',
            name='refresh_token',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='googleuser',
            name='token_uri',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
