# InterviewSimulator/views.py
import openai
from decouple import config
from django.shortcuts import render

openai.api_key = config('OPENAI_API_KEY')

def interview_view(request):
    # Define conversation_context within the function
    conversation_context = [
        {"role": "system", "content": "You are a helpful assistant."},
        # Add more context if needed
    ]
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=conversation_context
    )

    # Print the entire response for debugging
    print(response)

    # Get the assistant's reply
    assistant_reply = response['choices'][0]['message']['content']
    
    return render(request, 'interview_home.html', {'assistant_reply': assistant_reply})

