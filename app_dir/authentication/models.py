from django.db import models
from django.contrib.auth.models import Group
from structlog import get_logger

logger = get_logger(__name__)


class AbstractUser(models.Model):
    class Meta:
        abstract = True


class Role(models.Model):
    group = models.OneToOneField(Group, related_name="role")
    name = models.CharField(max_length=100)

    def add_user(self, user):
        user.groups.add(self.group)

    def remove_user(self, user):
        user.groups.remove(self.group)

    def __str__(self):
        return "{name}".format(name=self.name)
