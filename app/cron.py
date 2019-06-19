import os

from CR_BDE import settings
from .models import Report


def delete_file_orphan():
    list = os.listdir(settings.MEDIA_ROOT)
    image = Report.objects.all()
    imagelist = []
    for img in image:
        string = img.file.name
        imagelist.append(string)
    for img in list:
        if img not in imagelist:
            os.remove(settings.MEDIA_ROOT + "/" + img)