# I have created this file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def solution(request):
    djtext = request.POST.get("text", "default")

    status1 = request.POST.get("removepunc", "off")
    status2 = request.POST.get("uppercase", "off")
    status3 = request.POST.get("newlinerm", "off")
    status4 = request.POST.get("extraspacerm", "off")
    status5 = request.POST.get("getemail", "off")

    analyzed = ""
    if status1 == "on":
        punctuations = """!()-[]{};:'"\,<>./?@#$%^&*_~"""
        for i in djtext:
            if i not in punctuations:
                analyzed = analyzed + i

        djtext = analyzed
        analyzed = ""

    if status2 == "on":
        for i in djtext:
            analyzed = analyzed + i.upper()
        djtext = analyzed
        analyzed = ""

    if status3 == "on":
        for i in range(len(djtext)):
            if not(djtext[i] == '\n' or djtext[i] == '\r'):
                analyzed = analyzed + djtext[i]
        djtext = analyzed
        analyzed = ""

    if status4 == "on":
        for i in range(len(djtext)):
            if not(djtext[i] == " " and djtext[i+1] == " "):
                analyzed = analyzed + djtext[i]
        djtext = analyzed

    if status5 == "on":
        import re
        exp = r"\S+[-_.]?\S+@\S+[.]\S+"
        lst = re.findall(exp, djtext)
        params = {"purpose": "remove punctuations",
                  "analyzed_text": djtext, "email": lst}
        return render(request, "analyzer.html", params)

    if status1 == 'on' or status2 == 'on' or status3 == 'on' or status4 == 'on':
        params = {"purpose": "Required Answer", "analyzed_text": djtext}
        return render(request, "analyzer.html", params)
    else:
        return HttpResponse("Error")
