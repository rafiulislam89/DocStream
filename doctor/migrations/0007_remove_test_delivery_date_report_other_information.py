# Generated by Django 4.0.6 on 2022-09-08 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_test_specimen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='delivery_date',
        ),
        migrations.AddField(
            model_name='report',
            name='other_information',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
