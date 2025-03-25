from django.db import migrations


def populate_status(apps, schema_editor):
    entries = {
        "published": "A post visible to all users",
        "draft": "A post visible to the author only",
        "archived": "Older posts for logged in users"
    }
    Status = apps.get_model("posts", "Status")
    for key, value in entries.items():
        status_obj = Status(name=key, description=value)
        status_obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(populate_status)
    ]