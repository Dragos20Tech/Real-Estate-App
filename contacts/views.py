from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from contacts.models import Contact


# Create your views here.
def contact(request):
    # checks if the incoming HTTP request is a POST request
    if request.method == 'POST':
        # extracts form data from the request.POST dictionary
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if user has made inquiry already
        if request.user.is_authenticated:
            # Gets the id of the logged-in user
            user_id = request.user.id
            # Queries the Contact model to check if there is any entry where the listing_id matches the given
            # listing_id and the user_id matches the ID of the authenticated user
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/' + listing_id)

        # Creating a contact object
        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message,
                          user_id=user_id)
        # Saving a contact object in the database
        contact.save()

        # Send email
        # send_mail(
        #     'Property Listing Inquiry',
        #     'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info.',
        #     'dragospetrescu5@gmail.com',
        #     [realtor_email, 'wot.unicumgaming@gmail.com'],
        #     fail_silently=False
        # )

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
        return redirect('/listings/' + listing_id)
