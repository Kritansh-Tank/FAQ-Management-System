# Generated by Django 5.0.6 on 2025-02-01 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='translations',
        ),
        migrations.AddField(
            model_name='faq',
            name='question_bn',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_hi',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(),
        ),
    ]
