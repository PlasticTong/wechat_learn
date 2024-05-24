# Generated by Django 4.2.13 on 2024-05-22 07:59

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
            name='WeChatUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motto', models.CharField(blank=True, max_length=100, null=True)),
                ('pic', models.CharField(blank=True, max_length=50, null=True)),
                ('region', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=280)),
                ('pics', models.CharField(blank=True, max_length=100, null=True)),
                ('pub_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moments.wechatuser')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]