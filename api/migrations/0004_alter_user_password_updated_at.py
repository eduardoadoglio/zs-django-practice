# Generated by Django 3.2.19 on 2023-06-02 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_user_password_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password_updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
