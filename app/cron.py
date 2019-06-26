import os
from django.template.loader import render_to_string
from django.core.mail import send_mail
from CR_BDE import settings

from django.utils import timezone
from app.models import *


def delete_file_orphan():
    year_list = Year.objects.all()
    type_list = Type.objects.all()
    for year in year_list:
        for type in type_list:
            list = os.listdir(settings.MEDIA_ROOT+ "/" + year.folder_name + "/" + type.folder_name)
            report = Report.objects.filter(year=year).filter(type=type)
            filelist = []
            for rep in report:
                file = rep.file.name
                filelist.append(file)
            for img in list:
                if img not in filelist:
                    print (settings.MEDIA_ROOT+ "/" + year.folder_name + "/" + type.folder_name + "/" + img)
            print (filelist)
            print (list)


def send_cr():
    report = Report.objects.filter(email_sent=False).order_by("type", "-date")
    if report.count() > 0:
        html_content = render_to_string('app/email_send_cr.html', {'report_list': report, 'site': settings.ALLOWED_HOSTS[0], 'mois': timezone.now()})
        text_content = render_to_string('app/email_send_cr.txt', {'report_list': report, 'site': settings.ALLOWED_HOSTS[0]})
        send_mail(
            'Nouveaux CR BdE INSA Lyon',
            text_content,
            settings.DEFAULT_FROM_EMAIL,
            [settings.EMAIL_CR],
            html_message=html_content
        )
        report.update(email_sent=True)


def send_reminder_sg():
    report = Report.objects.latest("date")
    text_content = render_to_string('app/email_send_reminder_sg.txt', {'report': report, 'site': settings.ALLOWED_HOSTS[0]})
    send_mail(
        '[J-5] Diffusion CR',
        text_content,
        settings.DEFAULT_FROM_EMAIL,
        [settings.EMAIL_SG],
    )