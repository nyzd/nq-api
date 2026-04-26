from django.db import models
from django.db.models import Func


class UUIDv7(Func):
    function = "uuidv7"
    template = "%(function)s()"
    output_field = models.UUIDField()

    def deconstruct(self):
        path, args, kwargs = super().deconstruct()
        return path, list(args), kwargs
