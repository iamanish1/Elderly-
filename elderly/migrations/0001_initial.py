# Generated by Django 5.0 on 2024-03-24 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('doctor_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
                ('age', models.IntegerField()),
                ('experience', models.IntegerField()),
                ('speciality', models.CharField(max_length=15)),
                ('id', models.IntegerField()),
                ('location', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='hospitals',
            fields=[
                ('hospital_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=25)),
                ('ambulances', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='patients',
            fields=[
                ('patient_id', models.IntegerField(primary_key=True, serialize=False)),
                ('doctor_id', models.IntegerField()),
                ('name', models.CharField(max_length=15)),
                ('age', models.IntegerField()),
                ('medical_history', models.CharField(max_length=15)),
                ('allarges', models.CharField(max_length=15)),
                ('health_status', models.BooleanField()),
                ('mental_health', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='prescription',
            fields=[
                ('pres_id', models.IntegerField(primary_key=True, serialize=False)),
                ('patient_id', models.IntegerField()),
                ('doctor_id', models.IntegerField()),
                ('patient_name', models.CharField(max_length=15)),
                ('medecine', models.CharField(max_length=15)),
                ('reason', models.CharField(max_length=15)),
                ('Time_medication', models.CharField(max_length=15)),
            ],
        ),
    ]
