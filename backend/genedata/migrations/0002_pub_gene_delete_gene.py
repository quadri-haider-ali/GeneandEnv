# Generated by Django 4.1.2 on 2022-11-16 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genedata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pub_Gene',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120)),
                ('title', models.CharField(max_length=120)),
                ('pubmed_id', models.IntegerField(max_length=120)),
                ('keyword', models.CharField(max_length=120)),
                ('pubmed_url', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='Gene',
        ),
    ]