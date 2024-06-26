# Generated by Django 4.2.4 on 2023-08-18 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_remove_datapoint_country_remove_datapoint_end_year_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='datapoint',
            name='country',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='datapoint',
            name='end_year',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='datapoint',
            name='impact',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='datapoint',
            name='pestle',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='datapoint',
            name='sector',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='datapoint',
            name='source',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='datapoint',
            name='start_year',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='datapoint',
            name='topic',
            field=models.TextField(blank=True, null=True),
        ),
    ]
