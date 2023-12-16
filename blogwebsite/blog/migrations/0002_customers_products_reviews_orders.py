# Generated by Django 4.2.8 on 2023-12-16 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('rating', models.IntegerField(max_length=1)),
                ('review', models.IntegerField(max_length=1)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.customers')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.products')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(max_length=1)),
                ('created_At', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.customers')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.products')),
            ],
        ),
    ]
