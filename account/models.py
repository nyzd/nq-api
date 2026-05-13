from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# from core.models import Phrase
from core.expressions import UUIDv7


class CustomUser(AbstractUser):
    id = models.UUIDField(
        db_default=UUIDv7(), primary_key=True, editable=False, unique=True
    )
    first_name = None
    last_name = None
    display_name = models.CharField(max_length=255)
    birth_date = models.DateTimeField(blank=True, null=True)
    death_date = models.DateTimeField(blank=True, null=True)
    is_dead = models.BooleanField(default=False)


class UserName(models.Model):
    id = models.UUIDField(
        db_default=UUIDv7(), primary_key=True, editable=False, unique=True
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="names")
    language = models.CharField(max_length=3)
    phrase = models.ForeignKey(
        "core.Phrase", on_delete=models.CASCADE, related_name="names"
    )

    GIVEN_NAME = "given_name"
    FAMILY_NAME = "family_name"
    NASAB_NAME = "nasab_name"
    NICK_NAME = "nick_name"
    TITLE_NAME = "title_name"
    LAQAB_NAME = "laqab_name"
    KUNYAH_NAME = "kunyah_name"
    NISBAH_NAME = "nisbah_name"

    NAME_TYPE_CHOICES = [
        (GIVEN_NAME, "Given Name"),
        (FAMILY_NAME, "Family Name"),
        (NASAB_NAME, "Nasab"),
        (NICK_NAME, "Nick Name"),
        (TITLE_NAME, "Title"),
        (LAQAB_NAME, "Laqab"),
        (KUNYAH_NAME, "Kunyah"),
        (NISBAH_NAME, "Nisbah"),
    ]
    type = models.CharField(
        max_length=16,
        choices=NAME_TYPE_CHOICES,
    )
    text = models.TextField()
    is_primary = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
