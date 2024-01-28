from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import os
from dotenv import load_dotenv
from openai import OpenAI
from django.contrib.auth.models import User
from django.contrib import messages
from aiapp.form import RegisterForm, FeedBackForm

load_dotenv()
def ielts_checking(txt):
    api_key = os.getenv("demokey")

    if not api_key:
        return "API key not found. Please set your OpenAI API key."

    client = OpenAI(api_key=api_key)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f'''
            check this essay 
            {txt}

            answer about this essay like this :
            your ielts writing score: (write an approximate ielts writing task2 grade for this essay.)
            your mistakes:
        
            .......

            Here is a perfect example for your topic:
            (write here perfect essay example)
            
            display the answer nicely with design html and css code 
            kind off:
    <h1 style="font-family: 'Lucida Grande', Arial, sans-serif">An approximate IELTS Writing Task 2 grade for this essay is '5.5'  &#127882</h1>
    <h2 style="font-family: 'Lucida Grande', Arial, sans-serif">Your Mistakes &#128269;: </h2>
    <ul class="mistakes">
        <li>1 ....</li>
        <li>2 ...</li>
        <li>3...</li>
        <li>4 ...</li>
        <li>5 ...</li>
    </ul>
        <h2>Here is a perfect example for your topic: </h2>
        <p>essay ..........</p>
            make the design more beautiful beautiful 
            '''}
        ],
        model="gpt-3.5-turbo",
    )

    response_content = chat_completion.choices[0].message.content
    return response_content


def ielts_checking_view(request):
    if request.method == 'POST':
        essay_text = request.POST.get('essay_text', '')
        result = ielts_checking(essay_text)
        result_end = result
        return render(request, 'aiapp/essey.html', {'grade':result_end})
    return render(request, 'aiapp/home.html')



def dictionary(word):
    api_key = os.getenv("demokey")

    if not api_key:
        return "API key not found. Please set your OpenAI API key."

    client = OpenAI(api_key=api_key)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f'''
give information about this word '{word}'
answer like this 
<style>
    #definition,
    #examples 
        background-color: #f8f8f8;
        padding: 15px;
        margin-bottom: 20px;
        border-radius: 8px;
        box-shadow: 0 0 8px rgba(0, 0, 0, 0.1);
    

    h2 
        color: #333;
    

    p 
        color: #555;
        line-height: 1.6;
    
    strong 
        color: #007BFF;
    

    ol 
        list-style-type: decimal;
        padding-left: 20px;
    

    li 
        margin-bottom: 8px;
    
</style>

<h2>Definition:</h2>
<div id="definition">
    <p>"Find" is a verb that denotes the act of discovering or locating something, often as a result of searching,
        exploring, or investigating.</p>
</div>

<h2>Examples:</h2>
<div id="examples">
    <ol>
        <li><strong>Discovering something:</strong> While hiking in the woods, I found a beautiful waterfall.</li>
        <li><strong>Locating someone or something:</strong> I need to find my glasses before I can start reading.</li>
        <li><strong>Realizing or identifying something:</strong> After years of searching, he finally found his true
            passion in painting.</li>
        <li><strong>Meeting someone unexpectedly:</strong> I didn't expect to find my sister at the coffee shop; it was
            a pleasant surprise.</li>
    </ol>
</div>
continue write more information as much as possible
'''}
        ],
        model="gpt-3.5-turbo",
    )

    response_content = chat_completion.choices[0].message.content

    return response_content

def dict_view(request):
    if request.method == 'POST':
        word = request.POST.get('word', '')
        result = dictionary(word)
        return render(request, 'aiapp/dictionary.html', {'result':result,
                                                         'word':word})
    return render(request, 'aiapp/home.html')


def advice(topic):
    api_key = os.getenv("demokey")
    if not api_key:
        return "API key not found. Please set your OpenAI API key."
    client = OpenAI(api_key=api_key)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f'''
                write to this '{topic}' topic
                more ideas for writing essay ..
                write it on html like this 
                <h4> ......</h4>
'''}
        ],
        model="gpt-3.5-turbo",
    )

    response_content = chat_completion.choices[0].message.content

    return response_content


def advice_view(request):
    if request.method == 'POST':
        topic = request.POST.get('topic', '')
        result = advice(topic)
        return render(request, 'aiapp/advice.html', {'result':result})

    return render(request, 'aiapp/home.html')


def about(request):
    return render(request, 'aiapp/about.html')

def contact(request):
    return render(request, 'aiapp/contact.html')

def service(request):
    return render(request, 'aiapp/service.html')



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            User.objects.create(user=user)
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'aiapp/register.html', {'form': form})

@login_required
def feedback_view(request):
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            feedback_instance = form.save(commit=False)
            feedback_instance.user = request.user
            feedback_instance.save()
            messages.success(request, 'Thanks for your feedback!')
            return redirect('home-page')
    else:
        form = FeedBackForm()

    return render(request, 'aiapp/contact.html', {'form': form})