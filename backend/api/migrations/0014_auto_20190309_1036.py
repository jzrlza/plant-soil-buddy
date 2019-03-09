# Generated by Django 2.1.7 on 2019-03-09 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20190308_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='name',
        ),
        migrations.RemoveField(
            model_name='plantmoistlvl',
            name='plant_id',
        ),
        migrations.RemoveField(
            model_name='plantph',
            name='plant_id',
        ),
        migrations.AddField(
            model_name='plant',
            name='moist_data',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.PlantMoistLvl'),
        ),
        migrations.AddField(
            model_name='plant',
            name='ph_data',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.PlantPh'),
        ),
        migrations.AddField(
            model_name='plantmoistlvl',
            name='plant_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='plantph',
            name='plant_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]