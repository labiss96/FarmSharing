# Generated by Django 2.2.7 on 2019-11-22 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Successful_case_board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('writer', models.CharField(max_length=200, null=True)),
                ('body', models.CharField(max_length=200, null=True)),
                ('picture', models.CharField(max_length=200, null=True)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Team_recruitment_board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('region', models.CharField(max_length=200, null=True)),
                ('recruitment_number', models.IntegerField(default=0)),
                ('current_recruitment_condition', models.CharField(max_length=200, null=True)),
                ('active_period', models.IntegerField(default=0)),
                ('purpose', models.CharField(max_length=200, null=True)),
                ('body', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
