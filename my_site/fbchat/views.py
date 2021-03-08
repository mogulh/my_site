import json
import requests

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt



def post_facebook_message(fbid, recevied_message):
	    post_message_url = 'https://graph.facebook.com/v9.0/me/messages?access_token=EAAPu1Mk2t7IBADkoXQF69GwCiii3hwVNKZALfTRnwwcynNtp1mMoZA8Va8L8sjI7wzkwPp4BxYKFPi7Y9sJXllExU5zrASQJJxgiBvtFCuqdN9suvdwRlrWlHeLNu2KOFc0GdCHBfyXNq0E95dDzEzzbv2km2JZAMBXa2C7h0S49yJEMhvsV6SGGHukrVMZD'
	    response_msg = json.dumps({"recipient": {"id": fbid}, "message": {"text": recevied_message}})
	    status = requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=response_msg)
	    print(status.json())


class Home(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == '35014131':
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')



    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.body)
        # Converts the text payload into a python dictionary
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        # Facebook recommends going through every entry since they might send
        # multiple messages in a single call during high load
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                # Check to make sure the received call is a message call
                # This might be delivery, optin, postback for other events 
                print('entry', entry)
                print(message)
                if 'message' in message:
                    # Print the message to the terminal
                    print(message)
                    post_facebook_message(message['sender']['id'], message['message']['text'])
        return HttpResponse()


