from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    is_hospital = models.BooleanField(
        default=True
    )  # True если больница, False если аптека

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Организация")
        verbose_name_plural = _("Организации")


class CustomUser(AbstractUser):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="users",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")


class Appointment(models.Model):
    patient = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="appointments"
    )
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.patient.username} - {self.date} at {self.time}"

    class Meta:
        verbose_name = _("Запись на прием")
        verbose_name_plural = _("Записи на прием")
