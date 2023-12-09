from django.db import models

# Create your models here.

class MLModel(models.Model):
    SMILES = models.CharField(max_length=500)

    def __str__(self):
        return self.SMILES