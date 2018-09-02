# Generated by Django 2.1.1 on 2018-09-02 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ip', models.CharField(max_length=50)),
                ('status', models.BinaryField()),
                ('user', models.CharField(max_length=50, null=True)),
                ('userLogin', models.CharField(max_length=50, null=True)),
                ('password', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]