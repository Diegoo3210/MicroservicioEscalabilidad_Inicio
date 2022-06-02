from tokenize import Double
from venv import create
from django.db import models

# Create your models here.
from django.db import models

import os
import time
import hashlib
from os import path
from binascii import hexlify



def createHash():
    """This function generate 10 character long hash"""
    return hexlify(os.urandom(5))

class Document(models.Model):
    title = models.CharField(max_length = 200)
    uploadedFile = models.FileField(upload_to = "Uploaded Files/")
    hashNum = createHash()
    dateTimeOfUpload = models.DateTimeField(auto_now = True)