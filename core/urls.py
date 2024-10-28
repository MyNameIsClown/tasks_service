from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from modules.tasks.api.v1.views import TaskViewSet
from modules.boards.api.v1.views import BoardViewSet, BoardStatusViewSet

router = SimpleRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'boards', BoardViewSet)
router.register(r'board_status', BoardStatusViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
