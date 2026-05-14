from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note, Tag
from .forms import NoteForm


@login_required
def note_list(request):
    query = request.GET.get("q")
    tag_filter = request.GET.get("tag")

    notes = Note.objects.filter(user=request.user)

    if query:
        notes = notes.filter(text__icontains=query)

    if tag_filter:
        notes = notes.filter(tags__name__icontains=tag_filter)

    return render(request, "notes/list.html", {
        "notes": notes,
        "tags": Tag.objects.all()
    })


@login_required
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    return render(request, "notes/detail.html", {"note": note})


@login_required
def note_create(request):
    form = NoteForm(request.POST or None)

    if form.is_valid():
        note = form.save(commit=False)
        note.user = request.user
        note.save()
        form.save()
        return redirect("note_list")

    return render(request, "notes/form.html", {"form": form})


@login_required
def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)

    initial_tags = ", ".join([t.name for t in note.tags.all()])
    form = NoteForm(request.POST or None, instance=note, initial={"tags": initial_tags})

    if form.is_valid():
        form.save()
        return redirect("note_list")

    return render(request, "notes/form.html", {"form": form})


@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    note.delete()
    return redirect("note_list")