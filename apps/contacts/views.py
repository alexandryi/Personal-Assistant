from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta

from .models import Contact
from .forms import ContactForm, PhoneForm
from .services import get_upcoming_birthdays

@login_required
def contact_list(request):

    query = request.GET.get("q")

    contacts = Contact.objects.filter(user=request.user)

    if query:
        contacts = contacts.filter(name__icontains=query)

    upcoming = []

    today = date.today()

    days = int(request.GET.get("days", 7))

    for contact in contacts:

        if contact.birthday:

            birthday_this_year = contact.birthday.replace(
                year=today.year
            )

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(
                    year=today.year + 1
                )

            diff = (birthday_this_year - today).days

            if diff <= days:
                upcoming.append(contact)

    return render(
        request,
        "contacts/list.html",
        {
            "contacts": contacts,
            "upcoming": upcoming,
        }
    )


@login_required
def contact_create(request):

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            contact = form.save(commit=False)

            contact.user = request.user

            contact.save()

            return redirect("/contacts/")

    else:
        form = ContactForm()

    return render(
        request,
        "contacts/form.html",
        {"form": form}
    )


@login_required
def contact_edit(request, pk):

    contact = get_object_or_404(
        Contact,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":

        form = ContactForm(
            request.POST,
            instance=contact
        )

        if form.is_valid():
            form.save()
            return redirect("/contacts/")

    else:
        form = ContactForm(instance=contact)

    return render(
        request,
        "contacts/form.html",
        {"form": form}
    )


@login_required
def contact_delete(request, pk):

    contact = get_object_or_404(
        Contact,
        pk=pk,
        user=request.user
    )

    contact.delete()

    return redirect("/contacts/")


@login_required
def add_phone(request, pk):
    contact = get_object_or_404(Contact, pk=pk, user=request.user)
    form = PhoneForm(request.POST or None)

    if form.is_valid():
        phone = form.save(commit=False)
        phone.contact = contact
        phone.save()
        return redirect("contact_detail", pk=pk)

    return render(request, "contacts/form.html", {"form": form})


@login_required
def birthdays(request):
    contacts = get_upcoming_birthdays(request.user)
    return render(request, "contacts/list.html", {"contacts": contacts})

