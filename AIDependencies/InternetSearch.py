import requests
from bs4 import BeautifulSoup
import openai
from API_KEYS_FOR_FRIENDS import Open_AI_API

#Api keys
OPEN_AI_KEY=Open_AI_API

#TODO: Search a better way QueryAPI 
def DataFetch(Query):

    URL = "https://www.google.co.in/search?q=" + Query

    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
    }

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    #Find all information on the page
    results = soup.find_all("div")
    return results


def MessageFormat(message): 
    initialPrompt ={"role":"system","content":"your going to take infromation from HTML index and translate to a message"}
    chat_log=[initialPrompt,{"role":"user","content":f"Interpret this: {message}"}]
    response = openai.ChatCompletion.create( #TODO: trowing error of API limit
        model="gpt-3.5-turbo-16k-0613",
        messages=chat_log,
        temperature=1,
        stop=None
    )
    print(response['choices'][0]['message']['content'])

    return f"Interpret this information, you were asked for some info: {response['choices'][0]['message']['content']}"