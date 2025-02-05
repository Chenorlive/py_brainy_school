# Generated by Django 4.1.2 on 2023-03-25 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smssys', '0002_remove_myuser_nationalitytype_myuser_nationality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smssys.gendertypes'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='user_image'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='nationality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smssys.nationalitytype'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='password_hint',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
