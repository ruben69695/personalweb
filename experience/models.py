from django.db import models

# Create your models here.
class Job(models.Model):
    position_name = models.CharField(max_length=100, verbose_name="Position name")
    company = models.CharField(max_length=50, verbose_name="Company")
    description = models.TextField(verbose_name="Description", null=True, blank=True)
    from_date = models.DateField(verbose_name="From date")
    to_date = models.DateField(verbose_name="To date", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created date")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated date")

    class Meta:
        verbose_name = "job"
        verbose_name_plural = "jobs"
        ordering = ["-from_date"]

    def __str__(self):
        return self.company