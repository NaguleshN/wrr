# Generated by Django 4.2.4 on 2023-12-28 10:00

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
                ('event_name', models.CharField(max_length=20)),
                ('instruction', models.CharField(max_length=1000)),
                ('category', models.CharField(choices=[('technical', 'technical'), ('non-technical', 'non-technical')], max_length=14)),
                ('date', models.DateField()),
                ('mode', models.CharField(choices=[('online', 'online'), ('offline', 'offline')], max_length=10)),
                ('registration_fee', models.IntegerField()),
                ('prize_amount', models.IntegerField()),
                ('contact_number', models.BigIntegerField()),
                ('time', models.TimeField()),
                ('venue', models.CharField(max_length=50)),
            ],
        ),
    ]
