# Generated by Django 4.2.5 on 2024-01-14 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('logid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, verbose_name='username')),
                ('password', models.CharField(max_length=100, verbose_name='password')),
                ('role', models.CharField(max_length=10, verbose_name='role')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('u_name', models.CharField(max_length=100, verbose_name='u_name')),
                ('u_dob', models.CharField(max_length=100, verbose_name='u_dob')),
                ('u_email', models.CharField(max_length=100, verbose_name='u_email')),
                ('u_contact', models.CharField(max_length=100, verbose_name='u_contact')),
                ('u_address', models.CharField(max_length=300, verbose_name='u_address')),
                ('bloodgroup', models.CharField(max_length=300, verbose_name='u_bloodgroup')),
                ('u_log_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.login')),
            ],
        ),
        migrations.DeleteModel(
            name='Donation',
        ),
    ]
