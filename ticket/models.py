import datetime

from django.contrib.auth.models import User
from django.db import models


class TicketTag(models.Model):
    name = models.CharField(max_length=20, verbose_name="Etiket")

    def __str__(self):
        return self.name


class Ticket(models.Model):
    title = models.CharField(max_length=100, verbose_name="Başlık")
    short_desc = models.CharField(max_length=300, verbose_name="Kısa açıklama")
    long_desc = models.CharField(max_length=1000, verbose_name="Uzun açıklama", blank=True, null=True)
    creation_date = models.DateField(verbose_name="Olusturulma tarihi", default=datetime.date.today)
    end_date = models.DateField(verbose_name="Geçerlilik süresi", default=datetime.date.today)
    request_in_user = models.ForeignKey(User, related_name="requestinguser", verbose_name="Talepte Bulunan Kulanıcı")
    accepted = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    assigned_user = models.ForeignKey(User, related_name="assigned_user", verbose_name="Gönüllü", blank=True, null=True)
    tag = models.ManyToManyField(TicketTag, verbose_name="Etiket")
    progress = models.CharField(max_length=3, verbose_name="İşin tamamlanma oranı", blank=True, null=True)

    def __str__(self):
        return self.title
