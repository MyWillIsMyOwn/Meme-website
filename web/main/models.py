from django.db import models


class Photos(models.Model):
    title = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="images")

    def __str__(self):
        return f"id: {self.id};  owner: {self.owner};  picture: {self.picture};"

    class Meta:  # meta class is used for changing behavior of model fields
        managed = False
        db_table = "Photos"


class Comment(models.Model):
    photo = models.ForeignKey(
        Photos, related_name="allcomments", on_delete=models.CASCADE, null=True
    )
    owner_name = models.CharField(max_length=200)
    body = models.CharField(max_length=255)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"owner: {self.owner_name};  body: {self.body};  date: {self.add_date}; photo: {self.photo.id}"
