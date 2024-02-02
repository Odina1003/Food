# Generated by Django 5.0 on 2024-01-31 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breakfast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.IntegerField()),
                ('del_price', models.IntegerField(blank=True, null=True)),
                ('ball', models.IntegerField()),
                ('review', models.IntegerField()),
            ],
        ),
    ]
