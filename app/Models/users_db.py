from tortoise.models import Model
from tortoise import fields

class User(Model):
    userid = fields.CharField(max_length=100, pk=True)
    username = fields.CharField(max_length=100)
    password = fields.CharField(max_length=100)
    email = fields.CharField(max_length=200, unique=True)
    status = fields.BooleanField(default=True)
    role = fields.CharField(max_length=50, default="user")
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "users"
