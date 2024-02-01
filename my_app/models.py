from django.db import models

# Create your models here.
class Human(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female','Female' ),
        ('Others', 'Others'),

    )


    name = models.CharField(max_length = 25, unique = True)
    email = models.EmailField(max_length = 100, null=True, blank=True,)
    age = models.PositiveIntegerField(default = 20)
    gender = models.CharField(max_length = 25, choices = GENDER, null=True, blank=True, default='Male')
    image = models.ImageField(upload_to='images/', default='def.jpg')
    address = models.TextField(max_length=200, blank=True, null=True,)

    def __str__(self):
        return self.name
