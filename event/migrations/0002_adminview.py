# Generated by Django 4.2.7 on 2024-01-01 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminView',
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
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=20)),
            ],
        ),
    ]
