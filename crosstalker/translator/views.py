from django.shortcuts import render,HttpResponse
from gtts import gTTS
import os
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

def home(request):
    return HttpResponse('you have made it!')



@api_view(['GET'])
def to_speech(request):
    # text to speech
    tts(request.GET.get('text'),request.GET.get('lang'))
    return Response('Converted...')


def tts(text, lang):
    # Create a gTTS object
    tts = gTTS(text=text, lang=lang)

    # Save the speech to an audio file
    tts.save("./outputs/output.mp3")