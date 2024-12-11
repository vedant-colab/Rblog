from tortoise.models import Model
from tortoise import fields


class Session(Model):
    userid = fields.ForeignKeyField(model_name="models.User",  
        related_name="sessions", 
        on_delete=fields.CASCADE)
    token = fields.TextField(null=False)
    createdAt = fields.DatetimeField(auto_now_add=True)
    isActive = fields.BooleanField(default=True)
    
    class Meta:
        table = "sessions"
    