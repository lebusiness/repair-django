# Generated by Django 4.0.5 on 2022-07-04 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brigade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Название')),
                ('worker_count', models.IntegerField(verbose_name='Количество рабочих')),
                ('hour_price', models.IntegerField(verbose_name='Цена за час')),
            ],
            options={
                'verbose_name': 'Бригада',
                'verbose_name_plural': 'Бригада',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('descr', models.TextField(blank=True, verbose_name='Описание')),
                ('img', models.ImageField(upload_to='photos/caregories', verbose_name='Фото')),
                ('brigade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='repair.brigade', verbose_name='Бригада')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Chief',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Имя')),
                ('number', models.CharField(max_length=100, verbose_name='Номер')),
                ('experience', models.IntegerField(verbose_name='Стаж')),
            ],
            options={
                'verbose_name': 'Главный',
                'verbose_name_plural': 'Главный',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('descr', models.TextField(blank=True, verbose_name='Описание')),
                ('img', models.ImageField(upload_to='photos/services/', verbose_name='Фото')),
                ('hours', models.IntegerField(verbose_name='Часы Работы')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='repair.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуга',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='photos/portfolio/', verbose_name='Фото')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='repair.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Портфолио',
                'verbose_name_plural': 'Портфолио',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Имя')),
                ('text', models.TextField(blank=True, verbose_name='Отзыв')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='repair.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Отзывы',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='brigade',
            name='chief',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='repair.chief', verbose_name='Главный'),
        ),
    ]
