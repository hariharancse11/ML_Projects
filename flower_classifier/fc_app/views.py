import tempfile
from django.http import JsonResponse
from .classifier import predict

def home(request):
    if request.method == 'POST' and request.FILES.get('image'):
        # Get the uploaded image file
        image_file = request.FILES['image']

        # Save the image to a temporary file
        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as temp_file:
            temp_path = temp_file.name
            for chunk in image_file.chunks():
                temp_file.write(chunk)

        # Perform text prediction using the classifier
        text = predict(temp_path)

        # Delete the temporary file
        temp_file.close()
        # Uncomment the line below if you want to delete the file after prediction
        # os.remove(temp_path)

        # Return the predicted text as a JSON response
        return JsonResponse({'text': text})

    # Return an error message if no image is provided
    #return JsonResponse({'error': 'No image provided.'}, status=400)
    return ('hey you')