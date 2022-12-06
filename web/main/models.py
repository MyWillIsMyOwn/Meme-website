from django.db import models
from django.contrib.auth.models import User


class Photos(models.Model):
    title = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="images")
    likes = models.ManyToManyField(User, related_name="likes")

    def __str__(self):
        return f"id: {self.id};  owner: {self.owner};"

    @property
    def num_likes(self):
        return self.likes.all().count()

    class Meta:
        managed = True
        db_table = "Photos"


class Comment(models.Model):
    photo = models.ForeignKey(
        Photos, related_name="allcomments", on_delete=models.CASCADE, null=True
    )
    owner_name = models.CharField(max_length=200)
    body = models.CharField(max_length=255)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"owner: {self.owner_name};  body: {self.body};  date: {self.add_date}; photo id: {self.photo.id}"

    class Meta:
        managed = True
        db_table = "Comment"
