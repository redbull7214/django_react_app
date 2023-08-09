from django.shortcuts import get_object_or_404

from .models import Software


def create_software(title: str, price: float, currency: str, count: int) -> Software:
    """Create new software to DB."""

    new_obj = Software(title=title, price=price, currency=currency, count=count)
    new_obj.full_clean()
    new_obj.save()

    return new_obj


def get_software_list() -> list[Software]:
    """Select all software from db."""

    return Software.objects.all()


def get_software_by_id(id: int) -> Software | None:
    """Select software from db by id."""

    return get_object_or_404(Software, id=id)


def update_software(software: Software, data) -> Software:
    """Update software fiels."""

    for key, value in data.items():
        setattr(software, key, value)
    software.full_clean()
    software.save()
    return software


def delete_software(software: Software) -> None:
    """Delete software from db by id."""

    software.delete()
