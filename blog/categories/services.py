from .repositories import CategoryRepository
from blog.categories.models import Category
from core.errors import Messages, StatusCodes

class CategoryService:
    
    @staticmethod
    def get_all_categories():
        categories = CategoryRepository.get_all()
        return [{"id": category.id, "name": category.name} for category in categories]
    
    @staticmethod
    def create_category(name: str):
        if not name:
            return {"error": Messages.TITLE_REQUIRED, "status": StatusCodes.BAD_REQUEST}
        
        if CategoryRepository.exists_by_name(name):
            return {"error": Messages.UNIQUE_CATEGORY, "status": StatusCodes.BAD_REQUEST}
        
        category = CategoryRepository.create(name)
        return {"message": Messages.POST_CREATED, "id": category.id, "status": StatusCodes.CREATED}
    
    @staticmethod
    def update_category(category_id: int, name: str):
        if not name:
            return {"error": Messages.TITLE_REQUIRED, "status": StatusCodes.BAD_REQUEST}
        
        try:
            category = CategoryRepository.get_by_id(category_id)
        except Category.DoesNotExist:
            return {"error": Messages.POST_NOT_FOUND, "status": StatusCodes.NOT_FOUND}
        
        duplicates = CategoryRepository.filter_by_name_exclude_id(name, category_id)
        if duplicates.exists():
            duplicate_ids = [cat.id for cat in duplicates]
            return {
                "error": Messages.UNIQUE_CATEGORY, 
                "duplicate_id": duplicate_ids, 
                "status": StatusCodes.BAD_REQUEST
            }
        
        CategoryRepository.update(category, name)
        return {"message": Messages.POST_UPDATED, "status": StatusCodes.OK}
    
    @staticmethod
    def delete_category(category_id: int):
        try:
            category = CategoryRepository.get_by_id(category_id)
            CategoryRepository.delete(category)
            return {"message": Messages.POST_DELETED, "status": StatusCodes.OK}
        except Category.DoesNotExist:
            return {"error": Messages.POST_NOT_FOUND, "status": StatusCodes.NOT_FOUND}
