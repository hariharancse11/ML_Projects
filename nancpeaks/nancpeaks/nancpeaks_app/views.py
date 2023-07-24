from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
# Create your views here.
from gtts import gTTS
import os
from django.core.files.storage import default_storage
from .models import Speech
from django.views.decorators.csrf import csrf_exempt
from django.core.files import File



@csrf_exempt
@api_view(['GET'])
def to_speech(request):
    if request.method == 'GET':
        text = request.GET.get('text')
        language = request.GET.get('lang', 'en') 

        # Generate the speech using gTTS
        tts = gTTS(text=text, lang=language, slow=False)

        # Save the speech to an audio file in the local project folder
        project_folder = os.path.dirname(os.path.abspath(__file__))
        audio_file_path = os.path.join(project_folder, 'output.mp3')
        tts.save(audio_file_path)

        # Read the audio data from the file
        with open(audio_file_path, 'rb') as f:
            audio_data = f.read()

        # Return the audio file as an HTTP response with the correct content type
        response = HttpResponse(audio_data, content_type='audio/mpeg')
        response['Content-Disposition'] = 'attachment; filename="output.mp3"'

        return response

    return HttpResponse('Invalid request method.')



