# Generated by Django 3.1.4 on 2020-12-15 11:21

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
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('business_name', models.CharField(blank=True, max_length=200, null=True)),
                ('stage', models.CharField(choices=[('starting', 'starting'), ('achieving sales', 'achieving sales'), ('expansion', 'expansion')], default='starting', max_length=100)),
                ('paid_ads', models.BooleanField(default=False)),
                ('marketing_channels', models.CharField(blank=True, max_length=200, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('full_name', models.CharField(max_length=100)),
                ('services', models.CharField(choices=[('web development', 'web development'), ('marketing', 'marketing'), ('all', 'all')], max_length=20)),
                ('message', models.CharField(max_length=256)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('sub_to', models.CharField(choices=[('web development', 'web development'), ('marketing', 'marketing'), ('all', 'all')], default='all', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField()),
                ('duration_type', models.CharField(choices=[('month(s)', 'months(s)'), ('week(s)', 'week(s)'), ('year(s)', 'year(s)')], max_length=20)),
                ('target', models.IntegerField()),
                ('target_type', models.CharField(choices=[('web traffic', 'web traffic'), ('subscriptions', 'subscriptions'), ('sales', 'sales')], max_length=20)),
                ('start', models.IntegerField()),
                ('start_type', models.CharField(choices=[('month(s)', 'months(s)'), ('week(s)', 'week(s)'), ('year(s)', 'year(s)')], max_length=20)),
                ('business', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clients.business')),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.URLField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('dormant', 'dormant'), ('active no sales', 'active no sales'), ('with sales', 'with sales')], default='dormant', max_length=100)),
                ('business', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clients.business')),
            ],
        ),
    ]
