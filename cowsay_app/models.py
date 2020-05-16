from django.db import models


class Input(models.Model):
    body = models.CharField(max_length=280)

    def __str__(self):
        return self.body
