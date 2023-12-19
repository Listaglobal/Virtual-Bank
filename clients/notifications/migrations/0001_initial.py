# Generated by Django 4.2.7 on 2023-12-19 13:18

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
                ('notification_type', models.CharField(choices=[('USER_NOTIFICATION', 'User Notification'), ('TRANSACTION_NOTIFICATION', 'Transaction Alert'), ('ACCOUNT_NOTIFICATION', 'Account Alert'), ('SECURITY_NOTIFICATION', 'Security Notification')], max_length=30)),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('READ', 'Read'), ('UNREAD', 'Unread')], default='UNREAD', max_length=10)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
