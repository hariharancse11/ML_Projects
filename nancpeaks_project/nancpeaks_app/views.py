import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from gtts import gTTS
from .models import Speech
from django.conf import settings
import boto3

@api_view(['POST'])
def to_speech(request):
    text = request.data.get('text')
    lang = request.data.get('language')


    # Create a gTTS object and generate an MP3 file
    tts = gTTS(text,lang=lang)
    mp3_file_path = os.path.join(settings.MEDIA_ROOT, 'speech.mp3')
    tts.save(mp3_file_path)

    file_path = 'media/speech'+'.mp3'
    with open(file_path, 'rb') as file:
        audio = Speech()
        id = audio.audio.save(os.path.basename(file_path), file, save=True)

    audio_url = audio.audio.url
    
    return Response(audio_url)


