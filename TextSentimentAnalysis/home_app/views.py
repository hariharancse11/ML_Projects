from django.shortcuts import render
from rest_framework.response import Response
from textblob import TextBlob
from rest_framework.decorators import api_view
from rest_framework.views import APIView

@api_view(['POST'])
def predict(request):
    # Perform sentiment analysis

    text = request.data.get('sentence')
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    # Print the sentiment score
    return Response(sentiment)

@api_view(['GET'])
def home(request):
    return Response('You made it!')

