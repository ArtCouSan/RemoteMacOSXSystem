# Generated by Django 2.1.1 on 2018-09-02 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command', models.CharField(max_length=300)),
                ('category', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=50)),
                ('report', models.IntegerField(max_length=50)),
            ],
        ),
    ]
