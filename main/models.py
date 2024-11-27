from django.db import models
import uuid

branches = {
    ""
    "b":"Buxoro",
    "f":"Farg`ona",
    "o":"Olmaliq",
    "q":"Quvasoy",
    "s":"Samarqand",
    "sh":"Shahrisabz",
    "uc":"Uchquduq",
    "w":"Qarshi",
    "z":"Zarafshon"
            }

class Guest(models.Model):
    user = models.BigIntegerField()  # Link to the User model
    name = models.CharField(max_length=255)
    position_id=models.IntegerField()
    branch = models.CharField(max_length=255)  # Branch field (you can change it to TextField or another type if needed)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Automatically generates a unique UUID

    def __str__(self):
        return f"{self.name} - {self.branch}"

    @property
    def display_branch(self):
        return branches[self.branch]

class Comment(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    customer_id = models.PositiveBigIntegerField()
    comment = models.TextField()
    branch = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Comment by {self.guest.name} - {self.created_at.strftime('%d-%m-%Y %H:%M:%S')} - {self.branch}"
