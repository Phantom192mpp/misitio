# Generated by Django 3.1.2 on 2020-11-05 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestorDeProductos', '0006_auto_20201105_0219'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='password',
            field=models.TextField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
