from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from core.auth import api_key_required
from blog.categories.services import CategoryService
from core.errors import Messages, StatusCodes
import json

@csrf_exempt
def categories(request):
    if request.method == "GET":
        categories_data = CategoryService.get_all_categories()
        return JsonResponse({"categories": categories_data})

    elif request.method == "POST":
        return create_category(request)
    else:
        return JsonResponse({"error": Messages.METHOD_NOT_ALLOWED}, status=StatusCodes.METHOD_NOT_ALLOWED)

@csrf_exempt
@api_key_required
def create_category(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": Messages.INVALID_JSON}, status=StatusCodes.BAD_REQUEST)

    name = data.get("name")
    result = CategoryService.create_category(name)
    
    status = result.pop("status", StatusCodes.OK)
    return JsonResponse(result, status=status)

@csrf_exempt
@api_key_required
def update_category(request, category_id):
    if request.method != "PATCH":
        return JsonResponse({"error": Messages.METHOD_NOT_ALLOWED}, status=StatusCodes.METHOD_NOT_ALLOWED)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": Messages.INVALID_JSON}, status=StatusCodes.BAD_REQUEST)

    name = data.get("name")
    result = CategoryService.update_category(category_id, name)
    
    status = result.pop("status", StatusCodes.OK)
    return JsonResponse(result, status=status)

@csrf_exempt
@api_key_required
def delete_category(request, category_id):
    if request.method != "DELETE":
        return JsonResponse({"error": Messages.METHOD_NOT_ALLOWED}, status=StatusCodes.METHOD_NOT_ALLOWED)

    result = CategoryService.delete_category(category_id)
    status = result.pop("status", StatusCodes.OK)
    return JsonResponse(result, status=status)

@csrf_exempt
def category_router(request, category_id):
    if request.method == "PATCH":
        return update_category(request, category_id)
    elif request.method == "DELETE":
        return delete_category(request, category_id)
    else:
        return JsonResponse({"error": Messages.METHOD_NOT_ALLOWED}, status=StatusCodes.METHOD_NOT_ALLOWED)
