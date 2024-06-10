from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    contactEmail = models.EmailField(max_length=254)
    contactPhone = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Job(models.Model):

    class Type(models.TextChoices):
        Full_Time = "Full-Time"
        Part_Time = "Part-Time"
        Internship = "Internship"
        Remote = "Remote"
    
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=Type.choices)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    company = models.ForeignKey(Company, related_name="jobs", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (self.id, self.title) 