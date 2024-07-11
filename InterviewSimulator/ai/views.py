import numpy as np
from django.shortcuts import render
from sklearn.linear_model import LogisticRegression

def load_model():
    # Load the saved model
    model = np.load('ai/model.npy', allow_pickle=True).item()
    return model

def predict(request):
    if request.method == 'POST':
        features = [
            float(request.POST['feature1']),
            float(request.POST['feature2']),
            float(request.POST['feature3']),
            float(request.POST['feature4']),
        ]

        model = load_model()
        prediction = model.predict([features])
        context = {'prediction': prediction[0]}
        return render(request, 'ai/predict.html', context)

    return render(request, 'ai/predict.html')
