# Generated by Django 4.1.6 on 2023-02-12 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('dept_id', models.CharField(max_length=100, primary_key='True', serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('prn', models.CharField(max_length=100, primary_key='True', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('DOB', models.DateField(default='1998-01-01')),
                ('dept_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mycourse.dept')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=50, primary_key='True', serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycourse.dept')),
            ],
        ),
    ]
