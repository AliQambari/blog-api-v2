from django.db.models import QuerySet
from blog.categories.models import Category

class CategoryRepository:
    
    @staticmethod
    def get_all() -> QuerySet:
        return Category.objects.all()
    
    @staticmethod
    def get_by_id(category_id: int) -> Category:
        return Category.objects.get(id=category_id)
    
    @staticmethod
    def filter_by_ids(category_ids: list) -> QuerySet:
        return Category.objects.filter(id__in=category_ids)
    
    @staticmethod
    def filter_by_name(name: str) -> QuerySet:
        return Category.objects.filter(name=name)
    
    @staticmethod
    def filter_by_name_exclude_id(name: str, category_id: int) -> QuerySet:
        return Category.objects.filter(name=name).exclude(id=category_id)
    
    @staticmethod
    def create(name: str) -> Category:
        category = Category(name=name)
        category.save()
        return category
    
    @staticmethod
    def update(category: Category, name: str) -> Category:
        category.name = name
        category.save()
        return category
    
    @staticmethod
    def delete(category: Category) -> bool:
        category.delete()
        return True
    
    @staticmethod
    def exists_by_name(name: str) -> bool:
        return Category.objects.filter(name=name).exists()