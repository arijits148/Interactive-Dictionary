import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):                                                                                                                                                                                                                                            
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("did you mean {} instead?".format(get_close_matches(word, data.keys())[0]))
        yn = input("Enter Y for yes, N for no: ")
        if yn == "Y".lower():
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N".lower():
            return "The word doesn't exist. PLease check it again."
        else:
            return "Sorry, we didn't understand your querry."
    else:
        return "The word doesn't exist. PLease check it again."

new_word = input("Enter Word: ")

output = translate(new_word)

if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)
