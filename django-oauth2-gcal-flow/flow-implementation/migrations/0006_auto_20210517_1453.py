# Generated by Django 3.1.6 on 2021-05-17 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeblocker', '0005_googleuser_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='googleuser',
            name='id_token',
            field=models.CharField(max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='googleuser',
            name='refresh_token',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='googleuser',
            name='token',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
