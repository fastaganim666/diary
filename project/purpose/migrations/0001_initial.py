# Generated by Django 4.1.7 on 2023-03-20 15:46

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('main', models.BooleanField(default=False)),
                ('people', models.TextField(blank=True, default=None, null=True)),
                ('priority', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('deadline', models.DateField(blank=True, default=None, null=True)),
                ('add_date', models.DateField(auto_now_add=True)),
                ('achieved', models.BooleanField(default=False)),
                ('achievement_date', models.DateField(blank=True, default=None, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('completed', models.BooleanField(default=False)),
                ('completion_date', models.DateField(blank=True, default=None, null=True)),
                ('serial_number', models.IntegerField(blank=True, default=1, null=True)),
                ('purpose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purpose.purpose')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('completed', models.BooleanField(default=False)),
                ('completion_date', models.DateField(blank=True, default=None, null=True)),
                ('purpose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purpose.purpose')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('answer', models.TextField(blank=True, default=None, null=True)),
                ('date_add', models.DateField(auto_now_add=True)),
                ('date_answered', models.DateField(auto_now=True)),
                ('purpose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purpose.purpose')),
            ],
        ),
        migrations.CreateModel(
            name='Constraint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('completed', models.BooleanField(default=False)),
                ('completion_date', models.DateField(blank=True, default=None, null=True)),
                ('purpose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purpose.purpose')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('add_date', models.DateField(auto_now_add=True)),
                ('edit_date', models.DateField(auto_now=True, null=True)),
                ('purpose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purpose.purpose')),
            ],
        ),
    ]