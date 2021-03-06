# Generated by Django 4.0.5 on 2022-06-18 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата модификации')),
                ('deleted', models.BooleanField(default=False, verbose_name='Запись удалена')),
                ('num', models.PositiveIntegerField(verbose_name='Номер')),
                ('title', models.CharField(max_length=256, verbose_name='Тема')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_as_markdown', models.BooleanField(default=False, verbose_name='Тип MD')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.course')),
            ],
            options={
                'verbose_name': 'урок',
                'verbose_name_plural': 'уроки',
                'ordering': ('course', 'num'),
            },
        ),
    ]
