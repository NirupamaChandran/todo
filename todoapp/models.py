from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title=models.CharField(max_length=200)
    content=models.CharField(max_length=500,null=True)
    created_date=models.DateTimeField(auto_now_add=True,blank=True)
    user_object=models.ForeignKey(User,on_delete=models.CASCADE)
    status_options=(
        ("pending","pending"),
        ("completed","completed")
    )
    status=models.CharField(max_length=200,choices=status_options,default="pending")


    def __str__(self):
        return self.title