# Generated by Django 2.1.5 on 2019-02-15 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('years', models.IntegerField()),
                ('publish_date', models.DateField()),
                ('count', models.IntegerField(default=0)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.Author')),
            ],
        ),
    ]
