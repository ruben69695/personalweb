# Generated by Django 4.0.4 on 2022-06-20 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_technology_updated'),
        ('portfolio', '0002_auto_20190116_0701'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(to='core.technology', verbose_name='Technologies'),
        ),
    ]
