from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact

def contact_list(request):
    if request.method == "POST":
        name = request.POST.get("name")
        rollno = request.POST.get("rollno")
        contact = request.POST.get("contact")

        Contact.objects.create(
            name=name,
            rollno=rollno,
            contact=contact
        )
        return redirect("contact_list")

    contacts = Contact.objects.all()
    return render(request, "contact.html", {"contacts": contacts})


def contact_edit(request, id):
    contact_obj = get_object_or_404(Contact, id=id)

    if request.method == "POST":
        contact_obj.name = request.POST.get("name")
        contact_obj.rollno = request.POST.get("rollno")
        contact_obj.contact = request.POST.get("contact")
        contact_obj.save()
        return redirect("contact_list")

    return render(request, "edit.html", {"c": contact_obj})


def contact_delete(request, id):
    contact_obj = get_object_or_404(Contact, id=id)
    contact_obj.delete()
    return redirect("contact_list")
