from django.db import models

class Photos(models.Model):
    title = models.CharField(max_length=45)
    picture = models.TextField()

    class Meta:
        managed = False
        db_table = 'Photos'