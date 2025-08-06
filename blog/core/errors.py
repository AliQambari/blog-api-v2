class Messages:
    TITLE_REQUIRED = "Title is required"
    TEXT_REQUIRED = "Text is required"
    TITLE_TOO_LONG = "Title too long"
    TEXT_TOO_SHORT = "Text too short"
    TOO_MANY_CATEGORIES = "At most 6 categories can be added to a post."
    INVALID_CATEGORY_IDS = "Some category IDs are invalid"
    POST_NOT_FOUND = "Post not found"
    POST_CREATED = "Post created."
    POST_UPDATED = "Post updated successfully"
    POST_DELETED = "Post deleted"
    METHOD_NOT_ALLOWED = "Method not allowed"
    INVALID_JSON = "Invalid JSON"
    BAD_REQUEST = "Bad Request"
    UNIQUE_CATEGORY = "Categories must be unique"
    INVALID_PAGINATION_PARAMS  = "Invalid parameters. Use integers."
class StatusCodes:
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405