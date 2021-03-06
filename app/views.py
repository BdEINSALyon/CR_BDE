from django.http import FileResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

# Create your views here.
from app.models import *
from .forms import ReportForm


def home(request):
    year_list = Year.objects.all().order_by("-name")
    type_list = Type.objects.all()
    return render(request, 'app/home.html', {"year_list": year_list, "type_list": type_list})


def list_type(request, pk_year, pk_type):
    year = get_object_or_404(Year, pk=pk_year)
    type = get_object_or_404(Type, pk=pk_type)
    report_list = Report.objects.filter(year=year).filter(type=type).filter(is_public=True).order_by("-date")
    return render(request, 'app/list.html', {"year": year, "type": type, "report_list": report_list})


def list_year(request, pk_year):
    year = get_object_or_404(Year, pk=pk_year)
    report_list = Report.objects.filter(year=year).filter(is_public=True).order_by("-date")
    return render(request, 'app/list.html', {"year": year, "report_list": report_list})


def show_report(request, pk_report):
    report = get_object_or_404(Report, pk=pk_report)
    if not report.is_public:
        return HttpResponseForbidden()
    report.download_number = report.download_number + 1
    report.save()
    return FileResponse(open(report.get_url, 'rb'), content_type='application/pdf', filename='hello.pdf')


def add_report(request):
    form = ReportForm(request.POST or None, request.FILES or None)
    form.fields["year"].queryset = Year.objects.filter(upload_active=True)
    if form.is_valid():
        form.save()
        return redirect(reverse('home'))
    else:
        return render(request, 'app/add_report.html', {"form": form})


def edit_report(request, pk_report):
    report = get_object_or_404(Report, pk=pk_report)
    form = ReportForm(request.POST or None, request.FILES or None, instance=report)
    form.fields["year"].queryset = Year.objects.filter(upload_active=True)
    if form.is_valid():
        form.save()
        return redirect(reverse('home'))
    else:
        return render(request, 'app/add_report.html', {"form": form})
