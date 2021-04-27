# Generated by Django 3.1.8 on 2021-04-26 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('case_no', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('id_num', models.CharField(max_length=9, unique=True)),
                ('dob', models.DateField()),
                ('symp_date', models.DateField()),
                ('confirm_date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='users',
            name='chp_staff_no',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=1000)),
                ('x_coor', models.DecimalField(decimal_places=3, max_digits=7)),
                ('y_coor', models.DecimalField(decimal_places=3, max_digits=7)),
                ('event_date', models.DateField()),
                ('description', models.CharField(max_length=1000)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.case')),
            ],
        ),
    ]