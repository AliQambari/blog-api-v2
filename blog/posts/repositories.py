from django.db.models import QuerySet
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.posts.models import Post

class PostRepository:
    
    @staticmethod
    def get_all_ordered() -> QuerySet:
        return Post.objects.all().order_by("-updated_at")
    
    @staticmethod
    def get_by_id(post_id: int) -> Post:
        return Post.objects.get(id=post_id)
    
    @staticmethod
    def create(title: str, text: str, categories: QuerySet = None) -> Post:
        post = Post(title=title, text=text)
        post.save()
        if categories:
            post.categories.set(categories)
        return post
    
    @staticmethod
    def update(post: Post, title: str = None, text: str = None, categories: QuerySet = None) -> Post:
        if title:
            post.title = title
        if text:
            post.text = text
        if categories is not None:
            post.categories.set(categories)
        post.save()
        return post
    
    @staticmethod
    def delete(post: Post) -> bool:
        post.delete()
        return True
    
    @staticmethod
    def get_paginated_posts(posts: QuerySet, page: int, page_size: int) -> dict:
        try:
            page_size = int(page_size)
        except ValueError:
            page_size = 5

        paginator = Paginator(posts, page_size)

        try:
            posts_page = paginator.page(page)
        except PageNotAnInteger:
            posts_page = paginator.page(1)
        except EmptyPage:
            posts_page = paginator.page(paginator.num_pages)

        return {
            'posts_page': posts_page,
            'paginator': paginator
        }