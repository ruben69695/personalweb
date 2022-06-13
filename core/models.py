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