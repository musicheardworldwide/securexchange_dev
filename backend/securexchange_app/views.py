from django.http import JsonResponse
from django.views.decorators http import require_GET

@@require_GET
def health_check(request):
    "Health check endpoint to confirm api connectivity."
    return JSOnResponse({'status': 'ok'}, status=200)
