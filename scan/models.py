
from django.db import models, OperationalError, transaction
from django.template.defaultfilters import slugify
import json
from django_mysql.models import ListTextField
from django.utils import timezone
from lxml import html
import collections
import logging
from django.db.models import Count, CharField, Model
from django.urls import reverse
logger = logging.getLogger(__name__)
from datetime import datetime
from django.template.defaultfilters import truncatechars

class DataFile(models.Model):
    title = models.CharField(max_length=500,blank=True)







