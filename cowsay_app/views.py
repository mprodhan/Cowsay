from django.shortcuts import render
from cowsay_app.models import Input
from cowsay_app.forms import InputForm
import subprocess


def index(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Input.objects.create(
                body = data['body']
            )
            cow = subprocess.check_output(["cowsay", data['body']]).decode("utf-8")
            return render(request, "index.html", {"form": form, "cow": cow})
    form = InputForm()
    return render(request, "index.html", {"form": form})

def history_data(request):
    history = Input.objects.order_by('-id')[:10]
    info = ""
    for hist in history:
        info += subprocess.check_output(["cowsay", hist.body]).decode("utf-8")
    return render(request, "history.html", {"history": info})
