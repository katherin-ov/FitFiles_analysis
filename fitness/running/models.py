from django.db import models


class UploadFiles(models.Model):
    file = models.FileField(
        upload_to='uploads_model'
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )


class Result(models.Model):
    fit_file = models.OneToOneField(
        UploadFiles,
        on_delete=models.CASCADE,
        related_name='result'
    )
    sport = models.CharField(
        max_length=255
    )
    avg_speed = models.FloatField(
        help_text="m/s",
        blank=True,
        null=True
    )
    timestamp = models.DateTimeField()
    distance = models.FloatField(
        help_text="m",
        blank=True,
        null=True
    )
    total_calories = models.IntegerField(
        help_text="kcal",
        blank=True,
        null=True
    )
    avg_heart_rate = models.FloatField(
        help_text="bmp",
        blank=True,
        null=True
    )
    file_hash = models.CharField(
        max_length=255
    )
