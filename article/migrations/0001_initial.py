# Generated by Django 5.0.6 on 2024-06-24 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Blog title')),
                ('image', models.ImageField(upload_to='blog-img/')),
                ('details', models.TextField(verbose_name='Details')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('started_at', models.DateField(blank=True, null=True)),
            ],
        ),
    ]