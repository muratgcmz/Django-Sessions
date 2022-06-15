from django.urls import path, include
from rest_framework import routers
from .views import ( 
    home, 
#   hello_world, 
#   todoList, 
#   todoCreate, 
#   todoListCreate, 
#   todoUpdate, 
#   todoDelete
#    TodoList,
#    TodoDetail,
#    TodoListCreate,
#    TodoGetUpdateDelete,
    TodoMVS
 )

router = routers.DefaultRouter()
router.register('todos', TodoMVS)

urlpatterns = [
    path('', home),

    #! Function Based Views
    # path('hello/', hello_world),
    # path('todoList/', todoList),
    # path('todoCreate/', todoCreate),
    # path('todoListCreate/', todoListCreate),
    # path('todoUpdate/<int:pk>/', todoUpdate),
    # path('todoDelete/<int:pk>/', todoDelete),
    
    #! Class Based Views
    # path('list/', TodoListCreate.as_view()),
    # path("detail/<int:id>", TodoGetUpdateDelete.as_view()),
    path('', include(router.urls)),

]
