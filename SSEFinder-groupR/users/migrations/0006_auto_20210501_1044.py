# Generated by Django 3.1.8 on 2021-05-01 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210501_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('chp_staff_no', models.CharField(max_length=6)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email_ad', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUsers',
        ),
    ]