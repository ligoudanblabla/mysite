# Generated by Django 2.0.2 on 2018-04-04 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20180404_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_register',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
