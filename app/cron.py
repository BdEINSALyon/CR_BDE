import os
from django.template.loader import render_to_string
from django.core.mail import send_mail
from CR_BDE import settings
from django.utils import timezone
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


def send_cr():
    report = Report.objects.filter(email_sent=False)
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
    report = Report.objects.latest("-date")
    text_content = render_to_string('app/email_send_reminder_sg.txt', {'report': report, 'site': settings.ALLOWED_HOSTS[0]})
    send_mail(
        '[J-5] Diffusion CR',
        text_content,
        settings.DEFAULT_FROM_EMAIL,
        [settings.EMAIL_SG],
    )