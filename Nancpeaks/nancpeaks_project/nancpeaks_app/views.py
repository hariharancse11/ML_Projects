from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here
@api_view(['POST'])
def to_speech(request):
    from gtts import gTTS
    from pydub import AudioSegment

    text, speed = request.data.get('text'),request.data.get('speed')
    print(text,speed)

    # Create a gTTS object
    tts = gTTS(text)

    # Save the audio as a temporary file
    temp_file = "temp.mp3"
    tts.save(temp_file)

    # Load the audio file using pydub
    audio = AudioSegment.from_file(temp_file, format="mp3")
    print(temp_file)

    # Adjust the speed by changing the framerate
    speed_multiplier = speed  # Increase by 50%
    adjusted_audio = audio._spawn(audio.raw_data, overrides={
        "frame_rate": int(audio.frame_rate * speed_multiplier)
    })

    # Export the adjusted audio
    output_file = "output.mp3"
    adjusted_audio.export(output_file, format="mp3")

    # Delete the temporary file
    import os
    os.remove(temp_file)
    print("Text converted to speech")