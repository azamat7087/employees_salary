from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=40)
    salary = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0)])
    days = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    days_skipped = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    added_time = models.DateTimeField(auto_now_add=True,)
    last_updated = models.DateTimeField(auto_now=True, )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Employee"
        ordering = ['-salary']
