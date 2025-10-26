from django.urls import path, include
from . import views
# from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter 
from .views import CategoryViewSet ,NoteViewSet
# from .views import TaskViewSet , TagViewSet , CategoryViewSet ,NoteViewSet
from .views import VerifyEmail
from . views import TaskGeneric, TaskDetailGenetic
from rest_framework.routers import DefaultRouter
from task.views import activate_user


# router = DefaultRouter()
# router.register('', TaskViewSet )

# urlpatterns= router.urls
# urlpatterns =[
#     path('', views.home),
#     path('contact', views.contact),
#     # api
#     # # path('', views.index),
#     # path('apitask', views.TaskView.as_view()),
#     # path('apitask/<id>/', views.TaskDetail.as_view()),
   
#     path('apitag', views.tag),
#     path('apicategory' , views.category),
#     path('apitag/<id>/', views.showtag),
#     path('apicategory/<id>/', views.showcategory)
# ]

# urls.py


router = DefaultRouter()
# router.register(r'tasks', TaskViewSet),
# router.register(r'tags', TagViewSet),
router.register(r'category', CategoryViewSet),

# Nested router for notes under tasks
# sub_note = NestedDefaultRouter(router, 'tasks', lookup='task')
# sub_note.register(r'notes', NoteViewSet, basename='task-notes')

# router.register(r'notes', NoteViewSet),
urlpatterns = [
    # path('api', include(router.urls + sub_note.urls)),
    # path('', views.home),
    # path('contact', views.contact),
    path("tasks/", TaskGeneric.as_view()),
    path("tasks/<int:pk>/", TaskDetailGenetic.as_view()),
    path('activate/<uid>/<token>/', activate_user, name='verify_email'),
    path('verify-email/<uuid:token>/', VerifyEmail.as_view(), name='verify-email'),
]