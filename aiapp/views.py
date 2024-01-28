from django.shortcuts import render
import os
import re
from dotenv import load_dotenv
from openai import OpenAI

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
            like this <h1>your ielts writing score:</h1>....
            make the design text very beautiful 
            and '<!DOCTYPE html>
                <html lang="en">
                <head>
                <meta charset="UTF-8">
                <body>'
                 those parts don't need to be written
            '''}
        ],
        model="gpt-3.5-turbo",
    )

    # Extract relevant information from the model response
    response_content = chat_completion.choices[0].message.content
    # Parse the response and format it as needed
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



def about(request):
    return render(request, 'aiapp/about.html')

def contact(request):
    return render(request, 'aiapp/contact.html')

def service(request):
    return render(request, 'aiapp/service.html')