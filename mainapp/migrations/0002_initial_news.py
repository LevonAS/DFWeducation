from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0001_initial_courses"),
    ]

    operations = [
        migrations.CreateModel(
            name="News",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=256, verbose_name="Title")),
                ("preambule", models.CharField(max_length=1024, verbose_name="Preambule")),
                ("body", models.TextField(blank=True, null=True, verbose_name="Body")),
                ("body_as_markdown", models.BooleanField(default=False, verbose_name="As markdown")),
                ("created", models.DateTimeField(auto_now_add=True, verbose_name="Created")),
                ("updated", models.DateTimeField(auto_now=True, verbose_name="Edited")),
                ("deleted", models.BooleanField(default=False)),
            ],
        ),
    ]
