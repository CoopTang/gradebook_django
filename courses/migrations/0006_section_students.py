# Generated by Django 3.0.5 on 2020-04-02 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='students',
            field=models.ManyToManyField(to='courses.Student'),
        ),
    ]