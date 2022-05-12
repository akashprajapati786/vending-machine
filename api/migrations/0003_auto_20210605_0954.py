# Generated by Django 3.2.4 on 2021-06-05 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_money_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='money',
        ),
        migrations.AddField(
            model_name='transaction',
            name='dime',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='transaction',
            name='nickel',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='transaction',
            name='penny',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='transaction',
            name='quarter',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='transaction',
            name='total',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]