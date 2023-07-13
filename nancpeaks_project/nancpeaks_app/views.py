from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here
@api_view(['POST'])
def to_speech(request):
    from gtts import gTTS
    import os

    text = request.data.get('text')
    language = request.data.get('language')
    print(text, language)

    # Create a gTTS object
    tts = gTTS(text, lang=language)

    # Save the audio as a temporary file
    temp_file = "audio.mp3"
    tts.save(temp_file)

    audio_file_path = temp_file  # Replace with the actual audio file path

    print("Text converted to speech")

    with open(audio_file_path, 'rb') as f:
        audio_data = f.read()

    response = HttpResponse(audio_data, content_type='audio/mpeg')
    response['Content-Disposition'] = 'attachment; filename="audio.mp3"'

    # Delete the temporary audio file
    os.remove(temp_file)

    return response
