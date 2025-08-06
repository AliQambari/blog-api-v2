from django.http import JsonResponse
from functools import wraps

def api_key_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        api_key = request.headers.get("Auth-API-KEY")
        if api_key != "aqaq1212":
            return JsonResponse({"error": "Unauthorized"}, status=401)
        return view_func(request, *args, **kwargs)
    return wrapper