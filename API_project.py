
import pyfiglet

from termcolor import colored

msg = "Dad Joke 3000"

ascii_art = pyfiglet.figlet_format(msg)
colored_ascii = colored(ascii_art, color = "blue")
print(colored_ascii)

import requests
intro = input("Let me tell you a joke! Give me a topic (one word): ")
url = "https://icanhazdadjoke.com/search"
response = requests.get(url, headers = {"Accept": "application/json"}, params = {"term": intro}).json()  

print(response)


def dict2(dict1):
    for k, v in dict1.items():
        if k == "joke": 
            new_dict = {k: v for k, v in dict1.items()}
    return new_dict

dict2(response) 
answer = f"I've got {data["total_jokes"]} jokes about", f"{intro}. Here's one:"
print(answer)
