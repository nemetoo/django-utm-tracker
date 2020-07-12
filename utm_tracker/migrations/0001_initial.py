# Generated by Django 3.0.8 on 2020-07-12 20:48

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="LeadSource",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "medium",
                    models.CharField(
                        help_text="utm_medium: Identifies what type of link was used, such as cost per click or email.",
                        max_length=10,
                    ),
                ),
                (
                    "source",
                    models.CharField(
                        help_text="utm_source: Identifies which site sent the traffic, and is a required parameter.",
                        max_length=30,
                    ),
                ),
                (
                    "campaign",
                    models.CharField(
                        blank=True,
                        help_text="utm_campaign: Identifies a specific product promotion or strategic campaign.",
                        max_length=100,
                    ),
                ),
                (
                    "term",
                    models.CharField(
                        blank=True,
                        help_text="utm_term: Identifies search terms.",
                        max_length=50,
                    ),
                ),
                (
                    "content",
                    models.CharField(
                        blank=True,
                        help_text="utm_content: Identifies what specifically was clicked to bring the user to the site, such as a banner ad or a text link.",
                        max_length=50,
                    ),
                ),
                (
                    "timestamp",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text="When the event occurred.",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lead_sources",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"get_latest_by": ("timestamp",),},
        ),
    ]
