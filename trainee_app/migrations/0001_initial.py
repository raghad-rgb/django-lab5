# Generated by Django 5.1.6 on 2025-03-14 15:43

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course_app', '0002_track_alter_course_id_course_track'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('creation_date', models.DateField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, null=True, upload_to='trainee/imgs/')),
                ('course', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='course_app.course')),
                ('track', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course_app.track')),
            ],
        ),
    ]
