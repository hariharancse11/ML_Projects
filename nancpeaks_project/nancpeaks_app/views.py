from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here
@api_view(['POST'])
def to_speech(request):
    from gtts import gTTS
    from pydub import AudioSegment
    import os

    text,language = request.data.get('text'), request.data.get('language')
    print(text,language)

    # Create a gTTS object
    tts = gTTS(text, lang=language)

    # Save the audio as a temporary file
    temp_file = "audio.mp3"
    tts.save(temp_file)


    # # Load the audio file using pydub
    # audio = AudioSegment.from_file(temp_file, format="mp3")
    # print(temp_file)
    #
    # # Adjust the speed by changing the framerate
    # speed_multiplier = speed  # Increase by 50%
    # adjusted_audio = audio._spawn(audio.raw_data, overrides={
    #     "frame_rate": int(audio.frame_rate * speed_multiplier)
    # })
    #
    # # Export the adjusted audio
    # output_file = "audio.mp3"
    # adjusted_audio.export(output_file, format="mp3")

    audio_file_path = temp_file  # Replace with the actual audio file path

    print("Text converted to speech")

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