# Generated by Django 3.0.6 on 2020-05-21 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=200)),
                ('book_author', models.CharField(max_length=100)),
                ('book_published', models.DateTimeField(verbose_name='data published')),
                ('book_pages', models.PositiveSmallIntegerField()),
                ('book_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(verbose_name='data published'),
        ),
    ]
