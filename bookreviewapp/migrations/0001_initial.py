# Generated by Django 2.2 on 2019-04-11 08:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('contents', models.TextField()),
                ('price', models.CharField(max_length=100)),
                ('score', models.IntegerField(choices=[('1', 'ㅆㅎㅌㅊ'), ('2', 'ㅎㅌㅊ'), ('3', 'ㅍㅌㅊ'), ('4', 'ㅅㅌㅊ'), ('5', 'ㅆㅅㅌㅊ')])),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
