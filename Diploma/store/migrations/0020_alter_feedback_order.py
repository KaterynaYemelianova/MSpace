# Generated by Django 4.0.4 on 2022-06-10 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_freelanceorder_premium'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='order',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.composerorder'),
        ),
    ]
