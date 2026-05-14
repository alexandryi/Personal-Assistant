from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserFile
from .forms import FileForm


@login_required
def file_list(request):
    category = request.GET.get("category")

    files = UserFile.objects.filter(user=request.user)

    if category:
        files = files.filter(category=category)

    return render(request, "files/list.html", {
        "files": files,
        "categories": UserFile.CATEGORY_CHOICES
    })


@login_required
def file_upload(request):
    form = FileForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        file = form.save(commit=False)
        file.user = request.user
        file.save()
        return redirect("file_list")

    return render(request, "files/form.html", {"form": form})


@login_required
def file_delete(request, pk):
    file = UserFile.objects.get(pk=pk, user=request.user)
    file.delete()
    return redirect("file_list")