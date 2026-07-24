from django.db import models

class Seller(models.Model):
    name = models.CharField(max_length=255)
    business_name = models.CharField(max_length=255, blank=True, null=True)
    status     = models.CharField(max_length=255)
    Products_info=models.CharField(max_length=255)


    def __str__(self):
        return f"{self.name} (ID: {self.id})"

