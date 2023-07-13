from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from gtts import gTTS
from io import BytesIO
from django.http import HttpResponse

# Create your views here
@api_view(['POST'])
def to_speech(request):
    text = request.data.get('text')
    language = request.data.get('language')
    print(text, language)

    # Create a gTTS object
    tts = gTTS(text, lang=language)

    # Generate the audio data in memory
    audio_data = tts.get_audio_data()

    response = HttpResponse(audio_data, content_type='audio/mpeg')
    response['Content-Disposition'] = 'attachment; filename="audio.mp3"'

    return response

