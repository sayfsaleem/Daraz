# Generated by Django 4.2.7 on 2024-02-04 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_customuser_invite_link_alter_customuser_trx_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='reward_earning',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='invite_link',
            field=models.CharField(default='cb9cab02eb4f46b09ef591bbd7408633', max_length=50),
        ),
    ]
