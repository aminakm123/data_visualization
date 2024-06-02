# Generated by Django 4.2.4 on 2023-08-18 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_year', models.CharField(blank=True, max_length=10, null=True)),
                ('intensity', models.IntegerField(blank=True, null=True)),
                ('sector', models.CharField(blank=True, max_length=100, null=True)),
                ('topic', models.CharField(blank=True, max_length=100, null=True)),
                ('insight', models.TextField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('region', models.TextField(blank=True, max_length=100, null=True)),
                ('start_year', models.CharField(blank=True, max_length=10, null=True)),
                ('impact', models.CharField(blank=True, max_length=10, null=True)),
                ('added', models.DateTimeField(blank=True, null=True)),
                ('published', models.DateTimeField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('relevance', models.IntegerField(blank=True, null=True)),
                ('pestle', models.CharField(blank=True, max_length=100, null=True)),
                ('source', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('likelihood', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'datapoint',
                'verbose_name_plural': 'datapoints',
                'db_table': 'datapoint',
            },
        ),
    ]