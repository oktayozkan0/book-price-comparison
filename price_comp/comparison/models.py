from django.db import models

class Websites(models.Model):
    spider_name = models.CharField(max_length=20)
    website_title = models.CharField(max_length=20, default=None)
    working = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.website_title
