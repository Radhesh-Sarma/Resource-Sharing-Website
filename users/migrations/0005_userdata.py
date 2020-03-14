# Generated by Django 3.0.3 on 2020-03-14 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200310_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='userdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, verbose_name='email address')),
                ('content', models.TextField()),
            ],
        ),
    ]