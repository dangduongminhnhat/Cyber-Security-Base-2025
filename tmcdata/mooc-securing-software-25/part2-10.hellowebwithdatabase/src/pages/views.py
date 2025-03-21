from django.http import HttpResponse
from .models import Message


# Create your views here.

def homePageView(request):
    message_id = request.GET.get("id")
    if message_id and message_id.isdigit():
        message = Message.objects.get(pk=int(message_id))
        content = message.content
    return HttpResponse(content)
