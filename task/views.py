from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
#app/view.py
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task,Tag,Category, Note
from .serializers import TaskSerializer, TagSerializer, CategorySerializer ,NoteSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import generics, permissions

from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.http import JsonResponse

from task import models


# class TaskViewSet(ModelViewSet):
#     queryset = Task.objects.all()    
#     serializer_class =TaskSerializer
    
#     def get_queryset(self):
#         queryset = models.Task.objects.all()
#         category_id = self.request.query_params.get('category')
#         tag_id = self.request.query_params.get('tag')
#         if category_id is not None : 
#             queryset = models.Task.objects.filter(category_id = category_id)  #Each .filter() replaces the queryset with a new one.
#         if tag_id is not None : 
#             queryset = models.Task.objects.filter(tag = tag_id)               #If both category=1 and tag=2 are provided, only tag=2 is applied. category=1 gets ignored.
#         return queryset

class TaskGeneric(generics.ListCreateAPIView) :
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [ permissions.IsAuthenticated ]

    def get_queryset(self):
        if(self.request.user.is_superuser):
            return Task.objects.all()
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskDetailGenetic(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# class TaskViewSet(ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

#     def get_queryset(self):
#         queryset = models.Task.objects.all()
#         category_id = self.request.query_params.get('category')
#         tag_id = self.request.query_params.get('tag')

#         if category_id is not None:
#             queryset = queryset.filter(category_id=category_id)

#         if tag_id is not None:
#             queryset = queryset.filter(tag=tag_id)  # ✅ continues filtering the current queryset

#         return queryset

    
# class TagViewSet(ModelViewSet):
#     queryset = Tag.objects.annotate(
#         tags_count = Count('tasks')
#     )
#     serializer_class =TagSerializer
    
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(
        tasks_count = Count('tasks')
    )
    serializer_class =CategorySerializer
class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    
    def get_queryset(self):
        return Note.objects.filter(task=self.kwargs['task_pk'])
    
    def perform_create(self, serializer):
        task = Task.objects.get(pk=self.kwargs['task_pk'])
        serializer.save(task=task)
        # return super().get_queryset()
# # Create your views here.
# class TaskView(ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
    
    
    # def get_serializer_class(self):
    #     return TaskSerializer
# @api_view(['GET' , 'POST'])
# def task(request) :
#     if request.method == 'GET' :
#         all_task = Task.objects.all()
#         tasks = TaskSerializer(all_task , many =True)
#         return Response(tasks.data)
#     elif request.method == 'POST' :
#         client = TaskSerializer(data = request.data)
#         if client.is_valid() :
#             client.save()
#             return Response(client.data , status=201)
#         return Response(
#             client.errors , status=400)
        
# @api_view(['GET' , 'POST'])
# def tag(request) :
#     if request.method == 'GET' :
#         all_tag = Tag.objects.all()
#         tags = TagSerializer(all_tag , many =True)
#         return Response(tags.data)
#     elif request.method == 'POST' :
#         client = TagSerializer(data = request.data)
#         if client.is_valid() :
#             client.save()
#             return Response(client.data , status=201)
#         return Response(
#             client.errors , status=400)
    
# @api_view(['GET' , 'POST'])
# def category(request) :
#     if request.method == 'GET' :
#         all_category = Category.objects.all()
#         categorys = CategorySerializer(all_category , many =True)
#         return Response(categorys.data)
#     elif request.method == 'POST' :
#         client = CategorySerializer(data = request.data)
#         if client.is_valid() :
#             client.save()
#             return Response(client.data , status=201)
#         return Response(
#             client.errors , status=400)


# class TaskDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     lookup_field = 'id'
# @api_view(['GET' , 'PUT' , 'PATCH' , 'DELETE'])
# def showtask(request , id) :
#     task = get_object_or_404(Task, pk=id)
#     #query data to show use get_obj_or_404
#     if request.method == 'GET' :
#         x = TaskSerializer(task)
#         return Response(x.data)
    
#     elif request.method == 'PUT' :
#         client = TaskSerializer(task, data =request.data)
#         if client.is_valid():
#             client.save()
#             return Response(client.data)
#         return Response(client.errors, status=400)
    
#     elif request.method == 'PATCH' :
#         client = TaskSerializer(task, data =request.data, partial=True)
#         if client.is_valid():
#             client.save()
#             return Response(client.data)
#         return Response(client.errors, status=400)
#     elif request.method == 'DELETE' :
#         task.delete()
#         return Response({'message' : "delete :D"}, status=204)
    #show query data
    # return Response(f"show {id}")
    #show query data use trycatch
    # try :
    #     task = Task.objects.get(pk=id)
    #     x = TaskSerializer(task)
    #     return Response(x.data)
    # except :
    #     return Response({"error": "Something wrong"},
    #                     status=404)

@api_view()
def home(request):
    return render(request,'task/index.html')
# def index(request) : 
#     return Response("Hello from ST5")
@api_view()
def contact(request):
    return render(request,'task/contact.html')
# def show(request) :
#     return Response("Show")


# @api_view(['GET' , 'PUT' , 'PATCH' , 'DELETE'])
# def showtag(request , id) :
#     tag = get_object_or_404(Tag, pk=id)
#     #query data to show use get_obj_or_404
#     if request.method == 'GET' :
#         x = TagSerializer(tag)
#         return Response(x.data)
    
#     elif request.method == 'PUT' :
#         client = TagSerializer(tag, data =request.data)
#         if client.is_valid():
#             client.save()
#             return Response(client.data)
#         return Response(client.errors, status=400)
    
#     elif request.method == 'PATCH' :
#         client = TagSerializer(tag, data =request.data, partial=True)
#         if client.is_valid():
#             client.save()
#             return Response(client.data)
#         return Response(client.errors, status=400)
#     elif request.method == 'DELETE' :
#         tag.delete()
#         return Response({'message' : "delete :D"}, status=204)

# @api_view(['GET' , 'PUT' , 'PATCH' , 'DELETE'])
# def showcategory(request , id) :
#     category = get_object_or_404(Category, pk=id)
#     #query data to show use get_obj_or_404
#     if request.method == 'GET' :
#         x = CategorySerializer(category)
#         return Response(x.data)
    
#     elif request.method == 'PUT' :
#         client = CategorySerializer(category, data =request.data)
#         if client.is_valid():
#             client.save()
#             return Response(client.data)
#         return Response(client.errors, status=400)
    
#     elif request.method == 'PATCH' :
#         client = CategorySerializer(category, data =request.data, partial=True)
#         if client.is_valid():
#             client.save()
#             return Response(client.data)
#         return Response(client.errors, status=400)
#     elif request.method == 'DELETE' :
#         category.delete()
#         return Response({'message' : "delete :D"}, status=204)

class VerifyEmail(APIView):
    permission_classes = [AllowAny] 

    def get(self, request, token):
        return Response({"message": f"Email verified successfully! Token: {token}"})
    
User = get_user_model()

import os
from django.http import JsonResponse
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model

User = get_user_model()

def activate_user(request, uid, token):
    try:
        uid = urlsafe_base64_decode(uid).decode()
        user = User.objects.get(pk=uid)
    except (User.DoesNotExist, ValueError, TypeError, OverflowError):
        return JsonResponse({'detail': 'Invalid activation link'}, status=400)

    if default_token_generator.check_token(user, token):
        if not user.is_active:
            user.is_active = True
            user.save()

            current_host = os.environ.get("CURRENT_HOST")
            activation_url = f"{current_host}/api/verify-email/{uid}/{token}/"

            return JsonResponse({
                'detail': f'{user.username} account has been activated successfully.',
                'activation_url': activation_url
            }, status=200)
        else:
            return JsonResponse({'detail': 'Account already activated.'}, status=200)
    else:
        return JsonResponse({'detail': 'Activation link is invalid or expired.'}, status=400)
