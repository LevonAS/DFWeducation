from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0003_initial_lesson"),
    ]

    operations = [
        migrations.CreateModel(
            name="CourseTeachers",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name_first", models.CharField(max_length=128, verbose_name="Name")),
                ("name_second", models.CharField(max_length=128, verbose_name="Surname")),
                ("day_birth", models.DateField(verbose_name="Birth date")),
                ("deleted", models.BooleanField(default=False)),
                ("course", models.ManyToManyField(to="mainapp.Courses")),
            ],
        ),
    ]
