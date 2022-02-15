# Generated by Django 4.0.2 on 2022-02-15 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_room', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Дом',
                'verbose_name_plural': 'Дома',
            },
        ),
    ]