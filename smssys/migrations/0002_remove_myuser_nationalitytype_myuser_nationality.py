# Generated by Django 4.1.2 on 2023-03-24 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smssys', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='nationalityType',
        ),
        migrations.AddField(
            model_name='myuser',
            name='nationality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='smssys.nationalitytype'),
        ),
    ]
