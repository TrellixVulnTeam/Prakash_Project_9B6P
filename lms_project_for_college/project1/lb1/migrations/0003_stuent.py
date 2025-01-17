# Generated by Django 2.0 on 2019-07-27 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lb1', '0002_auto_20190727_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stuent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('semester', models.CharField(max_length=256)),
                ('student_id', models.PositiveIntegerField()),
                ('father_name', models.CharField(max_length=256)),
                ('mobile_no', models.PositiveIntegerField()),
                ('aadhar', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=256)),
                ('Pin_code', models.PositiveIntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='lb1.Book')),
            ],
        ),
    ]
