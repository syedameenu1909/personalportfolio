# Generated by Django 3.2.5 on 2021-11-06 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_remove_contact_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='portfolio/images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='service',
            name='description',
        ),
        migrations.RemoveField(
            model_name='service',
            name='image',
        ),
        migrations.RemoveField(
            model_name='service',
            name='url',
        ),
        migrations.AddField(
            model_name='service',
            name='brief',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='service',
            name='domainlist',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]