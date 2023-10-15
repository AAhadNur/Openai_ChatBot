import openai
from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from chatbot.settings import open_ai_api_key

from chat.models import Chat

# Create your views here.


openai_api_key = open_ai_api_key
openai.api_key = openai_api_key


def home(request):
    return render(request, 'chat/home.html')


def ask_openai(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an helpful assistant."},
            {"role": "user", "content": message},
        ]
    )

    answer = response.choices[0].message.content.strip()
    return answer


def chatbot(request):
    chats = Chat.objects.all()

    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        chat = Chat(user=request.user, message=message,
                    response=response, created_at=timezone.now())
        chat.save()
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chat/chatbot.html', {'chats': chats})
