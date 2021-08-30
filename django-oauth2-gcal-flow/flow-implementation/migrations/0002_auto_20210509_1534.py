# Generated by Django 3.1.6 on 2021-05-09 19:34

from django.db import migrations, models
import timeblocker.managers


class Migration(migrations.Migration):

    dependencies = [
        ('timeblocker', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='googleuser',
            managers=[
                ('objects', timeblocker.managers.GoogleUserOAuth2Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='googleuser',
            name='id',
            field=models.DecimalField(decimal_places=0, max_digits=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='googleuser',
            name='last_login',
            field=models.DateTimeField(null=True),
        ),
    ]