# simulator/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import openai
from decouple import config

openai.api_key = config('OPENAI_API_KEY')

def home(request):
    return render(request, 'simulator/home.html')

@login_required
def interview(request):
    if 'conversation' not in request.session:
        request.session['conversation'] = []

    conversation = request.session['conversation']

    if request.method == 'POST':
        user_message = request.POST.get('user_message', '')
        if user_message:
            # Append user message to the conversation
            conversation.append({"role": "user", "content": user_message})
            request.session['conversation'] = conversation

            # Generate a response from the AI
            prompt = "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in conversation])

            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt}
                    ]
                )
                bot_message = response['choices'][0]['message']['content'].strip()
                # Append bot message to the conversation
                conversation.append({"role": "interviewer", "content": bot_message})
                request.session['conversation'] = conversation

            except Exception as e:
                bot_message = f"Error generating response: {str(e)}"
                conversation.append({"role": "interviewer", "content": bot_message})
                request.session['conversation'] = conversation

    return render(request, 'simulator/interview.html', {
        'conversation': conversation,
    })

@login_required
def setup(request):
    return render(request, 'simulator/interview_setup.html')

@login_required
def setup_interview(request):
    if request.method == 'POST':
        # Extract form data
        subject_area = request.POST.get('subject_area')
        num_questions = request.POST.get('num_questions')
        difficulty_level = request.POST.get('difficulty_level')
        time_limit = request.POST.get('time_limit')
        industry = request.POST.get('industry')
        job_role = request.POST.get('job_role')
        skills = request.POST.get('skills')
        format = request.POST.get('format')
        question_type = request.POST.get('question_type')
        experience_level = request.POST.get('experience_level')

        # Check if any of the values are None or empty
        if not all([subject_area, num_questions, difficulty_level, time_limit, industry, job_role, skills, format, question_type, experience_level]):
            return render(request, 'simulator/setup_interview.html', {'error': 'All fields are required.'})

        # Generate the interview questions using OpenAI API
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an interview question generator."},
                    {"role": "user", "content": f"Generate {num_questions} {difficulty_level} interview questions for a {experience_level} candidate in the {industry} industry, applying for a {job_role} position with a focus on {skills}. The interview format is {format} and the questions should be {question_type}."},
                ]
            )
            
            # Process the response
            questions = response['choices'][0]['message']['content'].strip().split('\n')
            questions = [q for q in questions if q.strip()]  # Only include non-empty questions

            # Store generated questions in session
            request.session['interview_questions'] = questions
            
            # Redirect to the page where the user will answer the questions
            return redirect('answer_questions')
        except Exception as e:
            return render(request, 'simulator/setup_interview.html', {'error': str(e)})

    return render(request, 'simulator/setup_interview.html')


@login_required
def interview_home(request):
    if request.method == 'POST':
        # Collect all answers submitted by the user
        answers = []
        for key, value in request.POST.items():
            if key.startswith('answer_'):
                answers.append(value)
        
        # Create prompts to generate ideal answers
        ideal_answers = []
        for idx, answer in enumerate(answers):
            prompt = f"The following is a user's answer to an interview question:\n\nQuestion {idx + 1}: {request.session['interview_questions'][idx]}\n\nUser's Answer: {answer}\n\nPlease provide a more professionally appropriate answer."
            
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are an expert interview coach."},
                        {"role": "user", "content": prompt},
                    ]
                )
                ideal_answer = response['choices'][0]['message']['content'].strip()
                ideal_answers.append(ideal_answer)
            except Exception as e:
                ideal_answers.append(f"Error generating response: {str(e)}")

        return render(request, 'simulator/interview_home.html', {
            'interview_questions': request.session.get('interview_questions', []),
            'ideal_answers': ideal_answers
        })
    
    # If it's a GET request, render the initial questions
    interview_questions = request.session.get('interview_questions', [])
    return render(request, 'simulator/interview_home.html', {
        'interview_questions': interview_questions,
    })


@login_required
def answer_questions(request):
    interview_questions = request.session.get('interview_questions', [])
    
    if not interview_questions:
        return redirect('setup_interview')  # Redirect to setup if no questions are available

    if request.method == 'POST':
        answers = []
        for key, value in request.POST.items():
            if key.startswith('answer_'):
                answers.append(value)

        # Store user answers in session
        request.session['user_answers'] = answers

        # Redirect to the ideal answers page
        return redirect('ideal_answers')

    return render(request, 'simulator/answer_questions.html', {
        'interview_questions': interview_questions,
    })



@login_required
def ideal_answers_view(request):
    interview_questions = request.session.get('interview_questions', [])
    user_answers = request.session.get('user_answers', [])
    
    if not interview_questions or not user_answers:
        # Redirect to setup if no questions or answers are available
        return redirect('setup_interview')  

    ideal_answers = []
    for idx, answer in enumerate(user_answers):
        prompt = (
            f"The following is a user's answer to an interview question:\n\n"
            f"Question {idx + 1}: {interview_questions[idx]}\n\n"
            f"User's Answer: {answer}\n\n"
            f"Please provide a more professionally appropriate answer."
        ) #{idx + 1}
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert interview coach."},
                    {"role": "user", "content": prompt},
                ]
            )
            ideal_answer = response['choices'][0]['message']['content'].strip()
            ideal_answers.append(ideal_answer)
        except Exception as e:
            ideal_answers.append(f"Error generating response: {str(e)}")

    combined_data = zip(interview_questions, user_answers, ideal_answers)

    return render(request, 'simulator/ideal_answers.html', {
        'combined_data': combined_data,
    })
