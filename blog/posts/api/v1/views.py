from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from core.auth import api_key_required
from core.errors import Messages, StatusCodes
from posts.services import PostService
import json
from blog.categories.models import Category
from blog.core.const import CONST

@csrf_exempt
@api_key_required
def create_blog_post(request):
    if request.method != "POST":
        return JsonResponse({"error": Messages.METHOD_NOT_ALLOWED}, status=StatusCodes.METHOD_NOT_ALLOWED)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": Messages.BAD_REQUEST}, status=StatusCodes.BAD_REQUEST)

    title = data.get("title")
    text = data.get("text")
    category_ids = data.get("categories", [])

    result = PostService.create_post(title, text, category_ids)
    status = result.pop("status", StatusCodes.OK)
    return JsonResponse(result, status=status)

def list_blog_posts(request):
    page = request.GET.get("page", CONST.DEFAULT_PAGE)
    page_size = request.GET.get("page_size", CONST.DEFAULT_PAGE_SIZE)
    
    response = PostService.get_paginated_posts(page, page_size)
    return JsonResponse(response)

@csrf_exempt
def blog_posts(request):
    if request.method == "GET":
        return list_blog_posts(request)
    elif request.method == "POST":
        return create_blog_post(request)
    else:
        return JsonResponse({"error": Messages.METHOD_NOT_ALLOWED}, status=StatusCodes.METHOD_NOT_ALLOWED)

@csrf_exempt
@api_key_required
def get_post(request, post_id):
    if request.method != "GET":
        return JsonResponse({"error": Messages.METHOD_NOT_ALLOWED}, status=StatusCodes.METHOD_NOT_ALLOWED)

    result = PostService.get_post_by_id(post_id)
    status = result.pop("status", StatusCodes.OK)
    return JsonResponse(result, status=status)

@csrf_exempt
@api_key_required
def patch_post(request, post_id):
    if request.method != "PATCH":
        return JsonResponse({"error": Messages.METHOD_NOT_ALLOWED}, status=StatusCodes.METHOD_NOT_ALLOWED)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": Messages.BAD_REQUEST}, status=StatusCodes.BAD_REQUEST)

    title = data.get("title")
    text = data.get("text")
    category_ids = data.get("categories")

    result = PostService.update_post(post_id, title, text, category_ids)
    status = result.pop("status", StatusCodes.OK)
    return JsonResponse(result, status=status)

@csrf_exempt
@api_key_required
def delete_post(request, post_id):
    if request.method != "DELETE":
        return JsonResponse({"error": Messages.METHOD_NOT_ALLOWED}, status=StatusCodes.METHOD_NOT_ALLOWED)

    result = PostService.delete_post(post_id)
    status = result.pop("status", StatusCodes.OK)
    return JsonResponse(result, status=status)

def get_posts_by_category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return JsonResponse({"error": Messages.INVALID_CATEGORY_IDS}, status=StatusCodes.NOT_FOUND)

    posts = category.post_set.all() 
    post_data = [
        {
            "id": post.id,
            "title": post.title,
            "text": post.text[0:CONST.TRUNC_POST_TEXT],
            "created_at": post.created_at.isoformat(),
            "updated_at": post.updated_at.isoformat(),
        }
        for post in posts
    ]
    return JsonResponse({"category": category.name, "posts": post_data})

@csrf_exempt
def post_router(request, post_id):
    if request.method == "GET":
        return get_post(request, post_id)
    elif request.method == "PATCH":
        return patch_post(request, post_id)
    elif request.method == "DELETE":
        return delete_post(request, post_id)
    else:
        return JsonResponse({"error": Messages.METHOD_NOT_ALLOWED}, status=StatusCodes.METHOD_NOT_ALLOWED)
