from blog.posts.repositories import PostRepository
from blog.categories.repositories import CategoryRepository  
from blog.posts.models import Post
import re
from blog.core.errors import Messages, StatusCodes
from blog.core.const import CONST

def strip_html(text: str) -> str:
    return re.sub(r'<.*?>', '', text)

class PostService:
    
    @staticmethod
    def create_post(title: str, text: str, category_ids: list = None):
        if not title:
            return {"error": Messages.TITLE_REQUIRED, "status": StatusCodes.BAD_REQUEST}
        if not text:
            return {"error": Messages.TEXT_REQUIRED, "status": StatusCodes.BAD_REQUEST}
        
        title = strip_html(title)
        text = strip_html(text)

        if len(title) > CONST.MAX_TITLE_LENGTH:
            return {"error": Messages.TITLE_TOO_LONG, "status": StatusCodes.BAD_REQUEST}
        if len(text) < CONST.MIN_TEXT_LENGTH:
            return {"error": Messages.TEXT_TOO_SHORT, "status": StatusCodes.BAD_REQUEST}

        category_ids = category_ids or []
        if len(category_ids) > CONST.MAX_CATEGORY_LIMIT:
            return {"error": Messages.TOO_MANY_CATEGORIES, "status": StatusCodes.BAD_REQUEST}

        categories = []
        if category_ids:
            categories = CategoryRepository.filter_by_ids(category_ids)
            if categories.count() != len(category_ids):
                return {"error": Messages.INVALID_CATEGORY_IDS, "status": StatusCodes.BAD_REQUEST}

        post = PostRepository.create(title, text, categories)
        return {"message": Messages.POST_CREATED, "post_id": post.id, "status": StatusCodes.CREATED}
    
    @staticmethod
    def get_paginated_posts(page: int = 1, page_size: int = 5):
        try:
            page = int(page)
            page_size = int(page_size)
        except ValueError:
            return {
                "error": Messages.INVALID_PAGINATION_PARAMS,
                "status": StatusCodes.BAD_REQUEST
            }

        if page_size > CONST.MAX_PAGE_SIZE:
            page_size = CONST.MAX_PAGE_SIZE
        if page < CONST.DEFAULT_PAGE:
            page = CONST.DEFAULT_PAGE
        if page_size < CONST.MIN_PAGE_SIZE:
            page_size = CONST.DEFAULT_PAGE_SIZE

        posts = PostRepository.get_all_ordered()
        pagination_data = PostRepository.get_paginated_posts(posts, page, page_size)
        
        posts_page = pagination_data['posts_page']
        paginator = pagination_data['paginator']
        
        list_of_available_posts = []
        for post in posts_page:
            list_of_available_posts.append({
                "id": post.id,
                "title": post.title,
                "text": post.text[0:CONST.TRUNC_POST_TEXT],
                "created_at": post.created_at.isoformat(),
                "updated_at": post.updated_at.isoformat(),
                "categories": [category.name for category in post.categories.all()],
            })

        return {
            "count": paginator.count,
            "num_pages": paginator.num_pages,
            "current_page": posts_page.number,
            "posts": list_of_available_posts,
        }

    @staticmethod
    def update_post(post_id: int, title: str = None, text: str = None, category_ids: list = None):
        try:
            post = PostRepository.get_by_id(post_id)
        except Post.DoesNotExist:
            return {"error": Messages.POST_NOT_FOUND, "status": StatusCodes.NOT_FOUND}

        if title is not None:
            title = strip_html(title)
            if len(title) > CONST.MAX_TITLE_LENGTH:
                return {"error": Messages.TITLE_TOO_LONG, "status": StatusCodes.BAD_REQUEST}

        if text is not None:
            text = strip_html(text)
            if len(text) < CONST.MIN_TEXT_LENGTH:
                return {"error": Messages.TEXT_TOO_SHORT, "status": StatusCodes.BAD_REQUEST}

        categories = None
        if category_ids is not None:
            if len(category_ids) > CONST.MAX_CATEGORY_LIMIT:
                return {"error": Messages.TOO_MANY_CATEGORIES, "status": StatusCodes.BAD_REQUEST}
            categories = CategoryRepository.filter_by_ids(category_ids)
            if categories.count() != len(category_ids):
                return {"error": Messages.INVALID_CATEGORY_IDS , "status": StatusCodes.BAD_REQUEST}

        PostRepository.update(post, title, text, categories)
        return {"message": Messages.POST_UPDATED, "status": StatusCodes.OK}
    
    @staticmethod
    def delete_post(post_id: int):
        try:
            post = PostRepository.get_by_id(post_id)
            PostRepository.delete(post)
            return {"error": Messages.POST_DELETED, "status": StatusCodes.OK}
        except Post.DoesNotExist:
            return {"error": Messages.POST_NOT_FOUND, "status": StatusCodes.NOT_FOUND}
        
    @staticmethod
    def get_post_by_id(post_id: int):
        try:
            post = PostRepository.get_by_id(post_id)
            return {
                "id": post.id,
                "title": post.title,
                "text": post.text,
                "created_at": post.created_at.isoformat(),
                "updated_at": post.updated_at.isoformat(),
                "categories": [category.name for category in post.categories.all()],
                "status": StatusCodes.OK,
            }
        except Post.DoesNotExist:
            return {"error": Messages.POST_NOT_FOUND, "status": StatusCodes.NOT_FOUND}
