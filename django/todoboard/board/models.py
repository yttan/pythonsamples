# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible  # only if you need to support Python 2
# Create your models here.

class User(models.Model):
    username_text = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username_text

@python_2_unicode_compatible
class Comment(models.Model):
    comment_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.comment_text