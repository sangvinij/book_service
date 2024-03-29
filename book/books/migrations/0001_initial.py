# Generated by Django 4.1.7 on 2023-03-22 14:00

import django.core.validators
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/authors')),
                ('short_biography', models.TextField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='images/books')),
                ('year_published', models.CharField(max_length=4, validators=[django.core.validators.RegexValidator(regex='^\\d{1,4}$')])),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('author', models.ManyToManyField(to='books.author')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.genre')),
                ('theme', models.ManyToManyField(to='books.theme')),
            ],
        ),
        migrations.AddConstraint(
            model_name='author',
            constraint=models.UniqueConstraint(fields=('first_name', 'last_name'), name='unique_author'),
        ),
    ]
