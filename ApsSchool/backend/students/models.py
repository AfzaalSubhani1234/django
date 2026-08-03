from django.db import models
from accounts.models import User
# Create your models here.

class Student(models.Model):
    GENDER_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
    )


    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_profile"
    )


    roll_number = models.CharField(
        max_length=50,
        unique=True
    )


    father_name = models.CharField(
        max_length=100
    )


    date_of_birth = models.DateField()


    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )


    phone = models.CharField(
        max_length=20
    )


    address = models.TextField()


    admission_date = models.DateField(
        auto_now_add=True
    )


    def __str__(self):
        return self.user.full_name
