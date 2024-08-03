from django.shortcuts import render
from .models import Contact
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
#import messages
from django.contrib import messages
# Create your views here.


#accept whitout csrf_token
@csrf_exempt
def contact(request):
    if request.method == 'POST':
        #create a new contact
        contact = Contact.objects.create(
            name=request.POST.get('name', ''),
            email=request.POST.get('email', ''),
            phone=request.POST.get('phone', ''),
            message=request.POST.get('message', '')
        )
        contact.save()
        messages.success(request, 'Your message has been sent. Thank you!')
        #return back to the same place that send request
        response = redirect(request.META.get('HTTP_REFERER'))
        
        return response
        
