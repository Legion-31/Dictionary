import json
import difflib
from difflib import get_close_matches


data = json.load(open("data.json"))

def define(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]    
    elif  len(get_close_matches(word,data.keys())) > 0 :
        yn = input("Did you mean %s instead? Enter Y if yes and N if no: " % get_close_matches(word , data.keys())[0].upper())
        if yn == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == "N":
            return "Such word doesnt exist."
        else:
            return "We doesnt understand your entry."

    else :
        return ("You entered a wrong word , please check it.")


word=input("Enter any word to know its meaning : ")
output = (define(word))

if type(output) == list :
    for item in output:
        print(item)
else :
    print (output)
