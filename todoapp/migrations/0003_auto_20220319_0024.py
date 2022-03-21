# Generated by Django 3.0.4 on 2022-03-18 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_auto_20200516_0228'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='todo',
            name='is_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todoapp.Status'),
        ),
    ]