# Generated by Django 2.2.6 on 2019-11-03 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OurProject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shirt',
            name='picture_of_shirt',
            field=models.ImageField(height_field='Shirt.height', upload_to='C:/django1/virtual3/ItraProject', width_field='Shirt.width'),
        ),
    ]