from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
# Create your views here.
from gtts import gTTS
import os
from django.core.files.storage import default_storage
from .models import Speech
from django.core.files import File



@csrf_exempt
@api_view(['GET'])
def to_speech(request):
    text, language, speed = request.data.get('text'),request.data.get('language'),request.data.get('speed')
    # Example usage
    tts = gTTS(text=text, lang=language, slow=False)
    tts.speed = speed
    tts.save("output.mp3")

    audio_file_path = "output.mp3"  # Replace with the actual audio file path

    local_file_path = '/path/to/generated/file.mp3'
    with open(local_file_path, 'rb') as f:
        file_data = File(f)

    


    print("Text converted to speech")
    # audio = AudioSegment.from_mp3(audio_file_path)
    # new_file = speedup(audio,1.5,150)
    # new_file.export("file.mp3", format="mp3") 

    with open(audio_file_path, 'rb') as f:
        audio_data = f.read()

    response = HttpResponse(audio_data, content_type='audio/mpeg')
    response['Content-Disposition'] = 'attachment; filename="audio.mp3"'

    # Save the audio file in the local project folder
    project_folder = os.path.dirname(os.path.abspath(__file__))
    local_file_path = os.path.join(project_folder, 'audio.mp3')
    with open(local_file_path, 'wb') as f:
        f.write(audio_data)

    return response

