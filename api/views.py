from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import pickle
# Create your views here.
def home(request):
    data = {
        "age": "23",
        "qualification": "Degree"
    }
    return JsonResponse(data)

@api_view(['POST'])
def predict_iris(request):
    with open('ml_script/iris_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    data = request.data['features']
    prediction = model.predict([data])

    return Response({'prediction': prediction[0]})
