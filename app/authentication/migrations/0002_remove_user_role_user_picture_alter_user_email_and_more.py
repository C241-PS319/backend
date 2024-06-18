# Generated by Django 4.2.8 on 2024-06-17 13:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="role",
        ),
        migrations.AddField(
            model_name="user",
            name="picture",
            field=models.URLField(
                default="https://firebasestorage.googleapis.com/v0/b/nani-agritech.appspot.com/o/app%2Fauthentication%2Fdefault-user-photo.jpeg?alt=media&token=4f8585ca-908a-4d5f-941d-6c1965d18a3c"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=models.CharField(default="", max_length=20),
        ),
    ]