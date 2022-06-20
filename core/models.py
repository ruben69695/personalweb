from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Mensaje")

    class Meta:
        verbose_name = "mensaje"
        verbose_name_plural = "mensajes"
        ordering = ["-email"]

    def __str__(self):
        return self.email

class Technology(models.Model):
    name = models.CharField(max_length=25, verbose_name="Name", primary_key=True)
    created = models.DateTimeField(auto_now=True, verbose_name="Created date")

    class Meta:
        verbose_name = "technology"
        verbose_name_plural = "technologies"
        ordering = ["name"]

    def __str__(self):
        return self.name
