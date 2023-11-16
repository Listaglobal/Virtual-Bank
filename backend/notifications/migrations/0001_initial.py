# Generated by Django 4.2.7 on 2023-11-16 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.CharField(choices=[('TRANSACTION_ALERT', 'Transaction Alert'), ('ACCOUNT_UPDATE', 'Account Update'), ('SECURITY_NOTIFICATION', 'Security Notification')], max_length=30)),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('READ', 'Read'), ('UNREAD', 'Unread')], max_length=10)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]