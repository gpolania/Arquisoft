from django.db import models

class Appointment(models.Model):
    patient_name = models.CharField(max_length=255)
    doctor_name = models.CharField(max_length=255)
    date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[
        ("pending", "Pendiente"),
        ("confirmed", "Confirmada"),
        ("canceled", "Cancelada")
    ], default="pending")

    def __str__(self):
        return f"{self.patient_name} con {self.doctor_name} - {self.date}"
