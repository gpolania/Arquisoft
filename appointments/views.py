import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Appointment

# Simulación de pacientes y doctores
FAKE_PATIENTS = {1: "Juan Pérez", 2: "María Gómez"}
FAKE_DOCTORS = {2: "Dr. Rodríguez", 3: "Dra. Fernández"}

@csrf_exempt
def create_appointment(request):
    if request.method == "POST":
        data = json.loads(request.body)

        # Obtener ID y asignar nombres simulados
        patient_id = data.get("patient_id")
        doctor_id = data.get("doctor_id")

        patient_name = FAKE_PATIENTS.get(patient_id, "Paciente Desconocido")
        doctor_name = FAKE_DOCTORS.get(doctor_id, "Médico Desconocido")

        # Crear cita en la BD
        appointment = Appointment.objects.create(
            patient_name=patient_name,
            doctor_name=doctor_name,
            date=data.get("date")
        )

        return JsonResponse({
            "message": "Cita creada exitosamente",
            "appointment_id": appointment.id
        })

    return JsonResponse({"error": "Método no permitido"}, status=405)
