# Generated by Django 4.1.3 on 2022-11-25 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0003_remove_job_definition_jobseek_call_tatus_defenition_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusjob',
            name='status',
            field=models.CharField(choices=[('Открыта', 'Открыта'), ('Закрыта', 'Закрыта'), ('Заморожена', 'Заморожена')], max_length=300),
        ),
    ]
