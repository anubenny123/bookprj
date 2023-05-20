# Generated by Django 3.2.19 on 2023-05-20 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('author', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('isbn', models.CharField(max_length=100)),
            ],
        ),
    ]
