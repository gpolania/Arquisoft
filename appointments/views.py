import json
import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Appointment

def aleatorio():
    return random.random()

@csrf_exempt
def create_appointment(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            patient_id = data.get("patient_id")
            doctor_id = data.get("doctor_id")

            # Validaciones simuladas con probabilidades de fallo
            if aleatorio() > 0.9:
                return JsonResponse({"error": "Paciente no encontrado"}, status=400)
            if aleatorio() > 0.95:
                return JsonResponse({"error": "Paciente ya tiene una cita"}, status=400)
            if aleatorio() > 0.94:
                return JsonResponse({"error": "Doctor no encontrado"}, status=400)
            if aleatorio() > 0.85:
                return JsonResponse({"error": "Doctor ya tiene una cita"}, status=400)
            if aleatorio() > 0.9:
                return JsonResponse({"error": "Sala no disponible"}, status=400)
            if aleatorio() > 0.96:
                return JsonResponse({"error": "Maquinaria no disponible"}, status=400)

            # Crear cita en la BD
            appointment = Appointment.objects.create(
                patient_name=f"Paciente {patient_id}",
                doctor_name=f"Doctor {doctor_id}",
                date=data.get("date")
            )

            return JsonResponse({
                "message": "Cita creada exitosamente",
                "appointment_id": appointment.id
            })
        except json.JSONDecodeError:
            return JsonResponse({"error": "Formato JSON inválido"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Método no permitido"}, status=405)
