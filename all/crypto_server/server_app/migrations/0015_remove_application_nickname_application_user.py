# Generated by Django 4.1.3 on 2023-01-12 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server_app', '0014_application_nickname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='nickname',
        ),
        migrations.AddField(
            model_name='application',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='server_app.users', verbose_name='Продавец'),
        ),
    ]
