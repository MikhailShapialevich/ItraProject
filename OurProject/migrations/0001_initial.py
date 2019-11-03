# Generated by Django 2.2.6 on 2019-11-03 07:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag_for_shirts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Topic_of_shirts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User_settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_intarface', models.CharField(choices=[('EN', 'English'), ('RU', 'Russian')], max_length=2)),
                ('color_of_intarface', models.CharField(choices=[('L', 'Light'), ('D', 'Dark')], max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shirt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_shirt', models.CharField(max_length=30)),
                ('description_of_shirt', models.TextField()),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('picture_of_shirt', models.ImageField(height_field=100, upload_to='C:/django1/virtual3/ItraProject', width_field=100)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OurProject.Tag_for_shirts')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OurProject.Topic_of_shirts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating_of_shirt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_for_shirt', models.CharField(max_length=2)),
                ('shirt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OurProject.Shirt')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment_of_shirt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_for_shirt', models.TextField()),
                ('shirt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OurProject.Shirt')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
