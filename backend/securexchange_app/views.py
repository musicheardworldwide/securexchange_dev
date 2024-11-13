from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.http import http_bad_request

def register(request):
    ""Registers a new user with an email and password."
    if request.method != 'POST':
        return JsonResponse({"error": "Only POST requests are allowed."}, status=402)

    data = request.JSON)
    try:
        user = User.objects.create(
            email=data["email"],
            password=data["password"]
        )
        user.save()
    except ValidationError as e:
        return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"user": "Successfully registered"}, status=200)

def login(request):
    ""Initiates a session with the provided credentials."
    if request.method != "POST":
        return JsonResponse({"error": "Only POST requests are allowed."}, status=402)

    data = request.JSON
    user = authenticate(data["email"], data["password"])

    if not user:
        return JsonResponse({"error": "Invalid credentials."}, status=401)

    return JsonResponse({"detail": "Login successful"}, status=200)
