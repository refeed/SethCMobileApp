# Generated by Django 3.1.7 on 2021-03-21 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SETH', '0005_auto_20210321_0805'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='supported_certificates',
            field=models.ManyToManyField(blank=True, to='SETH.Certificate'),
        ),
    ]