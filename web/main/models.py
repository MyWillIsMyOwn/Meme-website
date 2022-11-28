from django.db import models


class Photos(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="images")

    def __str__(self):
        return self.title

    class Meta:  # meta class is used for changing behavior of model fields
        managed = False
        db_table = "Photos"
