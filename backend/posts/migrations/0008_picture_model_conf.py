# Generated by Django 4.2.2 on 2023-06-26 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_remove_answer_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='model_conf',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
