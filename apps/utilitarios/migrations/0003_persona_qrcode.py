# Generated by Django 2.1.3 on 2018-11-28 21:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('utilitarios', '0002_auto_20181118_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='qrcode',
            field=models.ImageField(blank=True, null=True, upload_to='qrcode'),
        ),
    ]
