# Generated by Django 2.2.14 on 2020-08-05 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10, unique=True, verbose_name='标题')),
                ('href', models.CharField(max_length=60, verbose_name='地址')),
                ('icon', models.CharField(max_length=60, verbose_name='图标')),
                ('order', models.IntegerField(verbose_name='顺序')),
            ],
            options={
                'verbose_name': '链接',
                'verbose_name_plural': '链接',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10, unique=True, verbose_name='标题')),
                ('href', models.CharField(max_length=60, verbose_name='地址')),
                ('order', models.IntegerField(verbose_name='顺序')),
            ],
            options={
                'verbose_name': '菜单',
                'verbose_name_plural': '菜单',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('abstract', models.CharField(blank=True, max_length=200)),
                ('body', models.TextField()),
                ('created_time', models.DateTimeField()),
                ('modified_time', models.DateTimeField()),
                ('views', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category')),
                ('tags', models.ManyToManyField(blank=True, to='blog.Tag')),
            ],
        ),
    ]
