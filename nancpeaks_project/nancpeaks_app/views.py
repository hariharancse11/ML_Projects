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

    # Generate the speech
    tts = gTTS(text, lang=lang)

    # Save the speech directly to S3 bucket
    s3 = boto3.client('s3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    bucket_name = 'nancpeaks'  # Replace with your S3 bucket name
    mp3_file_key = 'media/speech.mp3'  # Adjust the key or path in the bucket as needed

    s3.put_object(Body=tts.save_to_string(), Bucket=bucket_name, Key=mp3_file_key)

    # Get the URL of the uploaded file
    audio_url = f"https://{bucket_name}.s3.amazonaws.com/{mp3_file_key}"

    # Return the URL of the uploaded file as the response
    return Response(audio_url)

