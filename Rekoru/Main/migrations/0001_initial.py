# Generated by Django 4.1.7 on 2023-03-31 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddprojectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='title')),
                ('description', models.TextField(verbose_name='text')),
                ('imageproject', models.ImageField(upload_to='project-images/avatar/%Y-%m-%d/')),
                ('comments', models.TextField(blank=True, verbose_name='comments')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('username', models.CharField(blank=True, max_length=30, verbose_name='name')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff')),
                ('avatar', models.ImageField(blank=True, default='avatar_user.svg', upload_to='avatar/%Y-%m-%d/', verbose_name='avatar')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
