# Generated by Django 3.2.8 on 2021-12-07 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(blank=True, db_index=True, max_length=254, null=True, unique=True),
        ),
    ]
