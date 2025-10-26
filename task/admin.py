from datetime import date
from django.contrib import admin
from .models import Task, Category, Tag
# Register your models here.


@admin.register(Category)
class CategoryModel(admin.ModelAdmin):
    list_display=['id','name','hex_color','total_task']  
    def total_task(self, obj):
        return obj.tasks.count()
    total_task.short_description = 'Tasks'
    
        
@admin.register(Tag)
class TagModel(admin.ModelAdmin) :
    list_display=['id','label','total_task']  
    def total_task(self, obj):
        return obj.tasks.count()
    total_task.short_description = 'Tasks'
        

@admin.register(Task)
class TaskModel(admin.ModelAdmin) :
    list_display = ['id','name','due_date','category','tag_list','status']
    #list_editable = ['category']
    search_fields = ["name"]
    
    def tag_list(self, task) :
        return','.join(tag.label for tag in task.tag.all())  
    tag_list.short_description = 'tags'
    
    def status(self, task):
        if task.due_date:
            if task.due_date < date.today():
                return "Late"
            else:
                return "On Going"
        #return "No due date"
    status.short_description = 'Status'