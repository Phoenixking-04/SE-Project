# Generated by Django 5.1.5 on 2025-04-25 09:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0002_membership_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembershipPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Silver', 'Silver'), ('Gold', 'Gold'), ('Platinum', 'Platinum')], max_length=20, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('duration', models.CharField(choices=[('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Yearly', 'Yearly')], max_length=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'membership_plan',
            },
        ),
        migrations.AlterField(
            model_name='membership',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Pending', 'Pending'), ('Expired', 'Expired')], default='Active', max_length=10),
        ),
        migrations.AlterField(
            model_name='membership',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='memberships.membershipplan'),
        ),
    ]
