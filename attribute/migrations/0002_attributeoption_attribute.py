# Generated by Django 4.2.6 on 2023-10-26 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attributeoption',
            name='attribute',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='options', to='attribute.attribute'),
            preserve_default=False,
        ),
    ]