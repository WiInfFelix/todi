from rest_framework import routers

from .views import TodoViewSet

todo_router = routers.DefaultRouter()

todo_router.register("todos", TodoViewSet)

todo_urls = todo_router.urls