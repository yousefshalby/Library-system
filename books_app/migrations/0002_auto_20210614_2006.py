# Generated by Django 3.2.4 on 2021-06-14 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='pages',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='books_app.category'),
        ),
    ]
