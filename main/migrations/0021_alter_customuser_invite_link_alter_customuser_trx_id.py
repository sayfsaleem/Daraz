# Generated by Django 4.2.7 on 2024-02-04 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_customuser_invite_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='invite_link',
            field=models.CharField(default='facf50f48aa74e90bbe75074c428125c', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='trx_id',
            field=models.TextField(max_length=505),
        ),
    ]
