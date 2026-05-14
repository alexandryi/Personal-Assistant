from datetime import date, timedelta
from .models import Contact


def get_upcoming_birthdays(user, days=7):
    today = date.today()
    result = []

    contacts = Contact.objects.filter(user=user, birthday__isnull=False)

    for c in contacts:
        bday = c.birthday.replace(year=today.year)

        if bday < today:
            bday = bday.replace(year=today.year + 1)

        if 0 <= (bday - today).days <= days:
            result.append(c)

    return result