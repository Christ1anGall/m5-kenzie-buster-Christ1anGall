# Generated by Django 4.1.4 on 2022-12-10 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_is_employee"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_employee",
            field=models.BooleanField(),
        ),
    ]
