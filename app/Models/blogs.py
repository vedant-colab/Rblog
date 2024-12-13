from tortoise.models import Model
from tortoise import fields
from datetime import datetime

class Blogs(Model):
    blog_id = fields.BigIntField(primary_key = True)
    user_id = fields.ForeignKeyField(model_name="models.User", related_name="Blogs", on_delete=fields.CASCADE)
    title = fields.CharField(max_length=300, null=False, unique = False)
    body = fields.TextField(null = False, unique = False)
    slug = fields.CharField(max_length = 100,unique = True, null = False)
    created_at = fields.DatetimeField(auto_now_add = True)
    updated_at = fields.DatetimeField(auto_now = True)
    
    class Meta:
        table = "blogs"