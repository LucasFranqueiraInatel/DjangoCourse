# Generated by Django 3.1.2 on 2023-10-19 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0007_auto_20231018_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='cidade',
            name='descricao',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição'),
        ),
    ]