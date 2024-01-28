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
            (which sentences which grammatical errors)
            1. ....
            2. ....
            3. ....
            4. ....
            5. ....

            here is a perfect example for your topic:
            ..............
            ..............
            '''}
        ],
        model="gpt-3.5-turbo",
    )

    response_content = chat_completion.choices[0].message.content

    grade_match = re.search(r'Your IELTS writing score.*', response_content)
    mistakes_match = re.search(r'Your mistakes:(.*?)(?=Here is a perfect example for your topic:)', response_content, re.DOTALL)
    example_match = re.search(r'Here is a perfect example for your topic:(.*)', response_content, re.DOTALL)

    grade = grade_match.group(0).strip() if grade_match else "Оценка не найдена"
    mistakes = mistakes_match.group(0).strip() if mistakes_match else "Ошибки не найдены"
    example = example_match.group(0).strip() if example_match else "Пример не найден"

    dic_res = {
        'grade': grade,
        'mistakes': mistakes,
        'example':example
    }
    return dic_res

def ielts_checking_view(request):
    if request.method == 'POST':
        essay_text = request.POST.get('essay_text', '')
        result = ielts_checking(essay_text)
        return render(request, 'aiapp/essey.html', {'grade': result['grade'],
                                                   'mistakes':result['mistakes'],
                                                   'example':result['example']})
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
write it like this 

{word} - <definition>.

synonyms for the word :
......

antonyms for this word:
........

grammatical position:
........

examples using this word 
........
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
