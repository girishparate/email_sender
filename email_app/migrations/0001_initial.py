# Generated by Django 4.2 on 2023-06-24 08:13

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
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=1000)),
                ('body', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('sent_time', models.DateTimeField()),
                ('slug', models.SlugField()),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MailTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_time', models.DateTimeField()),
                ('mail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='email_app.mail')),
            ],
        ),
        migrations.CreateModel(
            name='EmailCredential',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smtp_provider', models.CharField(help_text='Enter smtp service provider', max_length=200)),
                ('port', models.SmallIntegerField(default=587)),
                ('email', models.EmailField(max_length=254)),
                ('email_password', models.CharField(help_text='Enter email password', max_length=200)),
                ('email_use_tls', models.BooleanField(default=True)),
                ('email_owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
